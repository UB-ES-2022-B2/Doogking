from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Profile, Housing
from .serializers import ProfileSerializer, HousingSerializer
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

class ResetView(APIView):
    queryset = Profile.objects.all()

    def get(self, request):
        request_email = request.data['email']
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
        request_otp = request.data['otp']
        request_pass = request.data['password']

        user = Profile.objects.get(otp=request_otp)
        user.set_password(request_pass)
        user.save()

        return Response({"message": "Password successfully changed!"})


