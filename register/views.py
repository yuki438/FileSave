from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from rest_framework_simplejwt.tokens import RefreshToken
from files.models import UserSpace
from .forms import RegisterForm

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    
    def post(self, request):
        button = request.POST.get('button')

        if button == 'Register':
            form = RegisterForm(request.POST)
            if form.is_valid():
                try:
                    user = form.save()

                    r = RefreshToken.for_user(user)
                    refresh_token = str(r)
                    access_token = str(r.access_token)

                    response = redirect('files')
                    response.set_cookie('refresh_token', refresh_token, httponly=True)
                    response.set_cookie('access_token', access_token, httponly=True)
                    return response

                except Exception as e:
                    messages.error(request, e)
                    return redirect('register')
            else:
                error = next(iter(form.errors.values()))[0]
                messages.error(request, error)
                return redirect('register')
        elif button == 'RedirectToLogin':
            return redirect('login')