from django.core.exceptions import PermissionDenied
from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .permissions import IsOwnerOfProfile
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import Profile, Housing, HousingImage, Reservation
from .serializers import ProfileSerializer, \
    CurrentProfileSerializer, \
    HousingSerializer, \
    HousingImageSerializer, \
    ReservationSerializer, \
    CustomerReservationSerializer, \
    ChangePasswordSerializer
import secrets
import requests
from django.conf import settings
from azure.storage.blob import BlobServiceClient
from rest_framework.generics import UpdateAPIView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView
from django.views.decorators.csrf import csrf_exempt


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('-date_joined')
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [
                permissions.IsAdminUser | IsOwnerOfProfile
            ]
        return [permission() for permission in permission_classes]

    @api_view(('DELETE',))
    def delete(request, id):
        profile = Profile.objects.get(id=id)
        if profile:
            profile.delete()
            return Response({"message": "Profile deleted"})


class HousingViewSet(viewsets.ModelViewSet):
    queryset = Housing.objects.all()
    serializer_class = HousingSerializer

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class HousingImageViewSet(viewsets.ModelViewSet):
    queryset = HousingImage.objects.all()
    serializer_class = HousingImageSerializer

    """
    Definition of a new action which will be associated with the
    "api/housing_images/housing/<housing_id> endpoint.
     It will be used to get only the images that belong
     to a house with a certain <housing_id>.
    """

    @action(detail=False)
    def select(self, request, housing_id=None):
        queryset = HousingImage.objects. \
            all(). \
            filter(housing__house_id=housing_id)
        serializer = HousingImageSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'list' or \
                self.action == 'retrieve' or \
                self.action == 'select':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'create':
            return CustomerReservationSerializer
        else:
            return ReservationSerializer

    def get_queryset(self):
        queryset = Reservation.objects.all()

        housing_id = self.request.query_params.get('housing')
        owner_id = self.request.query_params.get('owner')
        customer_id = self.request.query_params.get('customer')

        # Filter by housing if
        if housing_id:
            queryset = queryset.filter(
                housing__house_id=housing_id
            )

        # Filter by owner id
        if owner_id:
            # If the authenticated user is the owner,
            # show client details in each reservation
            if str(self.request.user.id) == owner_id:
                self.serializer_class = CustomerReservationSerializer
            queryset = queryset.filter(housing__house_owner__id=owner_id)

        # Filter by customer id (you can only query your own reservations)
        if customer_id:
            # Check if the authenticated user id is the same as the query id
            if str(self.request.user.id) == customer_id:
                self.serializer_class = CustomerReservationSerializer
                queryset = queryset.filter(customer__id=customer_id)
            else:
                raise PermissionDenied(
                    "You can't access other customers reservations!"
                )
        return queryset


class ResetView(APIView):
    queryset = Profile.objects.all()

    def get(self, request):
        request_email = request.query_params['email']
        otp = secrets.token_urlsafe(16)

        user = Profile.objects.get(email=request_email)
        user.otp = otp
        user.save()

        requests.post(
            url="https://api.emailjs.com/api/v1.0/email/send",
            json={"service_id": "service_doogking",
                  "template_id": "template_6flombd",
                  "user_id": "v_pteFmOs0hEWfD7U",
                  "template_params": {"email": request_email,
                                      "reset_code": otp}}
        )

        return Response({"message": "Password reset email sent!"})

    def post(self, request):
        request_email = request.data['email']
        request_otp = request.data['otp']
        request_pass = request.data['password']

        user = Profile.objects.get(email=request_email)
        if secrets.compare_digest(request_otp, user.otp):
            user.set_password(request_pass)
            user.otp = ""
            user.save()
            return Response({"message": "Password successfully changed!"})
        else:
            raise PermissionDenied("Email and reset token do not match!")


class ObtainAuthTokenUser(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(ObtainAuthTokenUser, self).post(
            request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = Profile.objects.get(id=token.user_id)
        return Response(
            {'token': token.key,
             'profile': CurrentProfileSerializer(user).data}
            )


class UploaderView(APIView):
    def post(self, request):
        file = request.FILES['file']
        credential = {"account_name": settings.AZURE_ACCOUNT_NAME,
                      "account_key": settings.AZURE_ACCOUNT_KEY}

        blob_service_client = BlobServiceClient(
            "https://" + settings.AZURE_CUSTOM_DOMAIN, credential)

        blob_client = blob_service_client.get_blob_client(
            container=settings.AZURE_CONTAINER, blob=file.name)
        blob_client.upload_blob(file.read())

        return Response({"message": "success", "uploaded_name": file.name})

class ChangePasswordView(UpdateAPIView):

    serializer_class = ChangePasswordSerializer
    model = Profile

    permission_classes = [permissions.IsAuthenticated]

    @csrf_exempt
    def get_permissions(self):

        permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    @csrf_exempt
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    @csrf_exempt
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)


        if serializer.is_valid():
            # Check old password
            # if not self.object.check_password(
            # serializer.data.get("old_password")):
            #       return Response({"old_password": ["Wrong password."]})
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {"message": "Password successfully changed!"}

            return Response(response)

class PasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    #template_name = 'registration/password_change_form.html'
    #title = _('Password change')

    #@method_decorator(sensitive_post_parameters())
    #@method_decorator(csrf_protect)
    #@method_decorator(login_required)
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    @csrf_exempt
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    @csrf_exempt
    def form_valid(self, form):
        form.save()
        # Updating the password logs out all other sessions for the user
        # except the current one.
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)



class ChangeView(UpdateAPIView):
    queryset = Profile.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ChangePasswordSerializer

    '''#@csrf_exempt
    def post(self,request,id):
        user = Profile.objects.get(id=id)
        request_pass = request.data['password']
        print("hola")
        print(request_pass)
        user.set_password(request_pass)
        user.save()
        return Response({"message": "Password successfully changed!"})'''

    def post(self, request):
        email = request.data['email']
        old_pass = request.data['old_password']
        new_pass = request.data['new_password']
        new_pass2 = request.data['new_password2']

        user = Profile.objects.get(email=email)
        if not user.check_password(old_pass):
            return Response({"old_password": ["Wrong password."]})
        if secrets.compare_digest(new_pass, new_pass2):
            user.set_password(new_pass)
            user.save()
            return Response({"message": "Password successfully changed!"})
        else:
            raise PermissionDenied("Email and reset token do not match!")
