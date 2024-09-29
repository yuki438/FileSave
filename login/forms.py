from django import forms
from django.contrib.auth import authenticate
from account.models import UserData

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserData
        fields = ['login', 'password']

    def clean(self):
        login = self.cleaned_data.get('login')
        password = self.cleaned_data.get('password')

        user = authenticate(login=login, password=password)
        if user is None:
            raise forms.ValidationError("Invalid login or password")
        return self.cleaned_data