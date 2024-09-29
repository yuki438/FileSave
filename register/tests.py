from django.test import TestCase
from django.contrib.auth import authenticate
from account.models import UserData
from .forms import RegisterForm

class RegisterTest(TestCase):
    def setUp(self):
        form = RegisterForm({
            'login': 'userr',
            'password': '1234',
        })
        form.save()
    def test_user_exist(self):
        user = authenticate(
            login='userr',
            password='1234',
        )
        self.assertIsNotNone(user)