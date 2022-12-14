from django.core.exceptions import PermissionDenied
from django.core.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .permissions import IsOwnerOfProfile
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import Profile, Housing, HousingImage, Reservation, Favourite
from .serializers import ProfileSerializer, \
    CurrentProfileSerializer, \
    HousingSerializer, \
    HousingImageSerializer, \
    ReservationSerializer, \
    DetailedReservationSerializer, \
    CustomerReservationSerializer, \
    FavouriteSerializer, \
    DetailedFavouriteSerializer, \
    ChangePasswordSerializer
import secrets
import requests
from django.conf import settings
from azure.storage.blob import BlobServiceClient
from rest_framework.generics import UpdateAPIView


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('-date_joined')
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        elif self.action == 'list':
            permission_classes = [permissions.IsAdminUser]
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

    def get_queryset(self):
        queryset = Housing.objects.all()

        cities = self.request.GET.getlist('city')
        owner = self.request.query_params.get('owner')
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        check_in = self.request.query_params.get('check_in')
        check_out = self.request.query_params.get('check_out')

        if cities:
            queryset = queryset.filter(city__in=cities)
        if owner:
            queryset = queryset.filter(house_owner__id=owner)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if check_in and check_out:
            # First get all reservations which overlap the given range
            booked = Reservation.objects.filter(
                start_date__lte=check_out,
                end_date__gte=check_in
            ).values('housing_id')
            # Get their associated house and exclude them
            queryset = queryset.exclude(house_id__in=booked)

        return queryset


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
            return DetailedReservationSerializer

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


class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer

    @action(detail=False, methods=['GET'])
    def select(self, request, user_id=None):
        queryset = Favourite.objects.filter(user__id=user_id)
        serializer = DetailedFavouriteSerializer(
            queryset,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    @action(detail=False, methods=['DELETE'])
    def delete(self, request):
        user_id = request.data['user']
        housing_id = request.data['housing']
        self.queryset.filter(user__id=user_id, housing_id=housing_id).delete()

        return Response({"message": "Successfully removed from favourites"})

    def get_permissions(self):
        permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class UpdateHousingRating(APIView):
    queryset = Housing.objects.all()
    url_kwargs = "housing_id"

    def post(self, request, housing_id):
        new_rating = request.data['rating']
        housing = self.queryset.get(house_id=housing_id)

        if housing:
            mean = (housing.rating +
                    (new_rating - housing.rating)/(housing.num_ratings+1))
            housing.rating = mean
            housing.num_ratings += 1
            housing.save()

            return Response({
                "message": "Rating successfully updated!",
                "rating": housing.rating
            })

        else:
            return Response({"message": "Could not update rating"}, 500)


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
             'profile': CurrentProfileSerializer(
                user,
                context={'request': request}
                ).data}
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
    queryset = Profile.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        email = request.data['email']
        old_pass = request.data['old_password']
        new_pass = request.data['new_password']
        new_pass2 = request.data['new_password2']

        user = Profile.objects.get(email=email)
        if not user.check_password(old_pass):
            raise ValidationError({"old_password": ["Wrong password."]})
        if secrets.compare_digest(new_pass, new_pass2):
            user.set_password(new_pass)
            user.save()
            return Response({"message": "Password successfully changed!"})
        else:
            raise ValidationError("No matching passwords")
