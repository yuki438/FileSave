from django.shortcuts import render, redirect
from django.views import View

class AppView(View):
    def get(self, request):
        print(request.user.login)
        context = {
            'login': request.user.login,
        }
        return render(request, 'app.html', context)
    def post(self, request):
        button = request.POST.get('button')

        if button == 'RedirectToFiles':
            return redirect('files')