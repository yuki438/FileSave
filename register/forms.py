from django import forms
from django.forms import ModelForm
from account.models import UserData

class RegisterForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserData
        fields = ['login', 'password']

    def save(self, commit=True):
        user = UserData.objects.create_user(
            login=self.cleaned_data['login'],
            password=self.cleaned_data['password']
        )
        return user