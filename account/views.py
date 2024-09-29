from django.shortcuts import render, redirect
from django.views import View

class AccountView(View):
    def get(self, request):
        context = {
            'login': request.user.login,
        }
        return render(request, 'account.html', context)
    def post(self, request):
        button = request.POST.get('button')

        if button == 'exit':
            response = redirect('register')
            response.delete_cookie('access_token')
            response.delete_cookie('refresh_token')
            return response