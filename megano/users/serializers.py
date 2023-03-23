from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['fullName', 'phone', 'email', 'avatar']


class ProfileAvatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['avatar']


class UserPasswordChangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['password']
