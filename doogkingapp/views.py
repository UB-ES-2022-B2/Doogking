from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Profile, Housing
from .serializers import ProfileSerializer, HousingSerializer
from .forms import SetPasswordForm
import secrets
import requests
from django.conf import settings
from azure.storage.blob import BlobServiceClient

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('-date_joined')
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
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
            SetPasswordForm
        else:
            raise PermissionDenied("Email and reset token do not match!")


'''#@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            return Response({"message": "Your password has been changed"})

        else:
            for error in list(form.errors.values()):
                return Response({"message": "Your password has been changed"})
                #messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, '', {'form': form})'''


class UploaderView(APIView):

    def post(self, request):
        file = request.FILES['file']
        credential = {"account_name": settings.AZURE_ACCOUNT_NAME, "account_key": settings.AZURE_ACCOUNT_KEY}

        blob_service_client = BlobServiceClient("https://" + settings.AZURE_CUSTOM_DOMAIN, credential)

        blob_client = blob_service_client.get_blob_client(container=settings.AZURE_CONTAINER, blob=file.name)
        blob_client.upload_blob(file.read())

        return Response({"message": "success", "uploaded_name": file.name})