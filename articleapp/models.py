# 35강

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model) :
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    # on_delete=models.SET_NULL 설정은, 회원 탈퇴시 게시글의 writer가 NULL값으로 되도록 하는 것

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)