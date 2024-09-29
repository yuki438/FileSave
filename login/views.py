from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from .serializers import CustomTokenObtainPairSerializer
from .forms import LoginForm

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    def post(self, request):
        button = request.POST.get('button')

        if button == 'Login':
            form = LoginForm(request.POST)
            if form.is_valid():
                serializer = CustomTokenObtainPairSerializer(data={
                    'login': form.cleaned_data['login'],
                    'password': form.cleaned_data['password']
                })
                try:
                    if serializer.is_valid(raise_exception=True):
                        tokens = serializer.validated_data
                        access_token = tokens.get('access')
                        refresh_token = tokens.get('refresh')

                        response = redirect('files')
                        response.set_cookie('access_token', access_token, httponly=True)
                        response.set_cookie('refresh_token', refresh_token, httponly=True)
                        return response
                except (AuthenticationFailed, ValidationError) as e:
                    messages.error(request, str(e))
                    return redirect('login')
            else:
                error = next(iter(form.errors.values()))[0]
                messages.error(request, error)
                return redirect('login')
        elif button == 'RedirectToRegister':
            return redirect('register')