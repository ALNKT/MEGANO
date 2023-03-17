from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework.response import Response
from rest_framework.views import APIView

from users.forms import UserRegistrationForm
from users.models import Profile
from users.serializers import ProfileSerializer


class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = "users/register.html"
    success_url = reverse_lazy('frontend:index')

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object, fullname=form.cleaned_data.get('fullname'),
                               phone=form.cleaned_data.get('phone'))
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user=user)
        return response


class ProfileView(APIView):

    def get(self, request):
        user = User.objects.get(pk=request.user.pk)
        user.phone = user.profiles.phone
        user.fullName = user.profiles.fullname
        serializer = ProfileSerializer(user, many=False)
        return Response(serializer.data)


class MyLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('login')
