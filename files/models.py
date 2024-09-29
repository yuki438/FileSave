from django.db import models
from account.models import UserData

class UserSpace(models.Model):
    user = models.OneToOneField(UserData, on_delete=models.CASCADE, related_name='space')

    def __str__(self):
        return f"{self.user.login}'s space"

class File(models.Model):
    sub_space = models.ForeignKey(UserSpace, on_delete=models.CASCADE, related_name='file')
    name = models.CharField(max_length=32, unique=True)
    uploaded_file = models.FileField(upload_to='files/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name