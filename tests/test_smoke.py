import pytest as pytest
from doogkingapp.models import Profile, Housing
import requests

...
import os


@pytest.mark.django_db  #
def test_views_main():
    response = requests.get("https://doogking.azurewebsites.net/")
    assert response.status_code == 200


@pytest.mark.django_db  #
def test_views_login():
    response = requests.get("https://doogking.azurewebsites.net/login")
    assert response.status_code == 200


@pytest.mark.django_db  #
def test_views_register():
    response = requests.get("https://doogking.azurewebsites.net/register")
    assert response.status_code == 200


@pytest.mark.django_db  #
def test_views_forgot_password():
    response = requests.get("https://doogking.azurewebsites.net/forgotPassword")
    assert response.status_code == 200


@pytest.mark.django_db  #
def test_views_reset():
    response = requests.get("https://doogking.azurewebsites.net/reset")
    assert response.status_code == 200

@pytest.mark.django_db  #
def test_database_housing():
    assert not Housing.objects.exists()