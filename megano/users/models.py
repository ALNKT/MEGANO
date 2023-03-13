from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profiles", verbose_name="пользователь")
    fullname = models.CharField(max_length=128, verbose_name='Ф.И.О.')
    phone = models.CharField(max_length=64, verbose_name='телефон')
    avatar = models.FileField(verbose_name='аватар')
