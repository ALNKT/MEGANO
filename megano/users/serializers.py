from django.contrib.auth.models import User
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    fullName = serializers.StringRelatedField()
    phone = serializers.StringRelatedField()
    email = serializers.StringRelatedField()
    avatar = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = ['fullName', 'phone', 'email', 'avatar']
