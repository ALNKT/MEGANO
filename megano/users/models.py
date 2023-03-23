from django.contrib.auth.models import User
from django.db import models


def upload_profile_avatar(instance: 'Profile', filename):
    return f'users/avatars/{instance.user.username}/{filename}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profiles", primary_key=True, verbose_name="пользователь")
    fullName = models.CharField(max_length=128, verbose_name='Ф.И.О.')
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=64, verbose_name='телефон')
    avatar = models.FileField(verbose_name='аватар', upload_to=upload_profile_avatar, blank=True, null=True)
