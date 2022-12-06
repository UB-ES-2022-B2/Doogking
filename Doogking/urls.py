"""Doogking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from doogkingapp import views
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'housing', views.HousingViewSet)
router.register(r'housing_images', views.HousingImageViewSet)
router.register(r'reservations', views.ReservationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/login/', views.ObtainAuthTokenUser.as_view()),
    path('admin/', admin.site.urls),
    path('api/reset/', views.ResetView.as_view()),
    path('api/deleteProfile/<int:id>', views. ProfileViewSet.delete,
         name='delete'),
    path('api/upload/', views.UploaderView.as_view()),
    path('api/change-password/', views.ChangePasswordView.as_view(),
         name='change-password'),
    url(r'^api/housing_images/housing/(?P<housing_id>[0-9]+)/$',
        views.HousingImageViewSet.as_view({'get': 'select'})),

    url(r'^.*$', TemplateView.as_view(template_name='index.html')),
]
