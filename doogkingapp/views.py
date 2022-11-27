from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import Profile, Housing, HousingImage, Reservation
from .serializers import ProfileSerializer, CurrentProfileSerializer, HousingSerializer, HousingImageSerializer, ReservationSerializer, CustomerReservationSerializer
import secrets
import requests

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('-date_joined')
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

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
    Definition of a new action which will be associated with the "api/housing_images/housing/<housing_id> endpoint.
     It will be used to get only the images that belong to a house with a certain <housing_id>.
    """
    @action(detail=False)
    def select(self, request, housing_id=None):
        queryset = HousingImage.objects.all().filter(housing__house_id=housing_id)
        serializer = HousingImageSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve' or self.action == 'select':
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

    def get_queryset(self):
        queryset = Reservation.objects.all()

        housing_id = self.request.query_params.get('housing')
        owner_id = self.request.query_params.get('owner')
        customer_id = self.request.query_params.get('customer')

        # Filter by housing if
        if housing_id:
            queryset = queryset.filter(housing__house_id=housing_id)
        
        # Filter by owner id
        if owner_id:
            # If the authenticated user is the owner, show client datails in each reservation
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
                raise PermissionDenied("You can't access other customers reservations!")
        return queryset
    

class ResetView(APIView):
    queryset = Profile.objects.all()

    def get(self, request):
        request_email = request.query_params['email']
        otp = secrets.token_urlsafe(16)

        user = Profile.objects.get(email=request_email)
        user.otp = otp
        user.save()

        requests.post(\
                url= "https://api.emailjs.com/api/v1.0/email/send",
                json = {"service_id":"service_doogking", "template_id":"template_6flombd", "user_id":"v_pteFmOs0hEWfD7U", "template_params":{"email": request_email, "reset_code": otp} }
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
        response = super(ObtainAuthTokenUser, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = Profile.objects.get(id=token.user_id)
        return Response({'token': token.key, 'profile': CurrentProfileSerializer(user).data })
