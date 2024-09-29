from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import UploadForm, FilterForm
from .models import UserSpace, File
import os

class FilesView(View):
    def get(self, request):
        space = UserSpace.objects.filter(user=request.user).first()
        files = File.objects.filter(sub_space=space)
        total_files = files.count()
        form1 = UploadForm()
        form2 = FilterForm(request.GET)
        
        if form2.is_valid():
            filter_choice = form2.cleaned_data['filter']

            if filter_choice == 'date':
                files = files.order_by('created_at')
            elif filter_choice == 'name':
                files = files.order_by('name')

        context = {
            'login': request.user.login, 
            'space': space,
            'files': files,
            'total_files': total_files,
            'form1': form1,
            'form2': form2,
        }

        return render(request, 'files.html', context)
    
    def post(self, request):
        button = request.POST.get('button')

        if button == 'CreateSpace':
            UserSpace.objects.create(user=request.user)

        elif button == 'AddFile':
            form = UploadForm(request.POST, request.FILES)
            if form.is_valid():
                file_instance = form.save(commit=False)
                file_instance.sub_space = UserSpace.objects.get(user=request.user)

                ext = os.path.splitext(file_instance.uploaded_file.name)[1]
                file_instance.uploaded_file.name = f"{file_instance.name}{ext}"

                file_instance.save()
            else:
                error = next(iter(form.errors.values()))[0]
                messages.error(request, error)
                
        return redirect('files')