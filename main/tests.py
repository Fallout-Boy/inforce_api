import pytest

from rest_framework.test import APIClient
from django.contrib.auth.models import User

from .models import Restaurant


@pytest.mark.django_db
def test_employee_registration():
    client = APIClient()

    response = client.post('/api/register/', {
        'username': 'Max',
        'password': '12345678'
    })

    assert response.status_code == 201
    assert User.objects.filter(username='Max').exists()


@pytest.mark.django_db
def test_jwt_login():
    User.objects.create_user(username='Max', password='12345678')
    client = APIClient()

    response = client.post('/api/token/', {
        'username': 'Max',
        'password': '12345678'
    })

    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data


@pytest.mark.django_db
def test_create_restaurant():
    user = User.objects.create_user(username='admin', password='pass')
    client = APIClient()
    token = client.post('/api/token/', {
        'username': 'admin',
        'password': 'pass'
    }).data['access']

    client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
    response = client.post('/api/restaurants/', {
        'name': 'Test Restaurant',
        'description': 'some description'
    })

    assert response.status_code == 201
    assert Restaurant.objects.filter(name='Test Restaurant').exists()
