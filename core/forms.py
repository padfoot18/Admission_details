from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.forms import EmailInput, TextInput, PasswordInput


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'first_name', 'middle_name', 'last_name', 'is_teacher', 'is_student')
        widgets = {
            'email': EmailInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'middle_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields
