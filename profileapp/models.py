from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile/', null = True)
    # image가 저장되는 root를 upload_to로 지정해준다.
    # media밑에 profile이라는 폴더 아래의 경로로 저장될 것이다.
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)