import pytest as pytest
from doogkingapp.models import Profile, Housing
import requests
from django.urls import reverse
from rest_framework.authtoken.views import obtain_auth_token
from django.test import Client

c = Client()

@pytest.mark.django_db  #
def test_views_main():
    response = c.get("http://127.0.0.1:8000/")  # get the path for the list of contacts
    assert response.status_code == 200


@pytest.mark.django_db  #
def test_views_login():
    response = c.get("http://127.0.0.1:8000/login")
    assert response.status_code == 200


@pytest.mark.django_db  #
def test_views_register():
    response = c.get("http://127.0.0.1:8000/register")
    assert response.status_code == 200


@pytest.mark.django_db  #
def test_views_forgot_password():
    response = c.get("http://127.0.0.1:8000/forgotPassword")
    assert response.status_code == 200


@pytest.mark.django_db  #
def test_views_reset():
    response = c.get("http://127.0.0.1:8000/reset")
    assert response.status_code == 200

@pytest.mark.django_db  #
def test_database_housing():
    assert not Housing.objects.exists()

@pytest.mark.django_db  #
def test_database_profile():
    assert not Profile.objects.exists()
