from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'core/homepage.html')


class UserSignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'core/signup.html'


@login_required(login_url='/user/login/')
def profile(request):
    return render(request, 'core/user_profile.html')
