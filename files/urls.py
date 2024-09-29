from django.urls import path
from .views import FilesView

urlpatterns = [
    path('', FilesView.as_view(), name='files'),
]