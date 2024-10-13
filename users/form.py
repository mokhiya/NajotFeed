from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import UserModel


def validate_image_size(image):
    max_size = 5 * 1024 * 1024  # 5MB in bytes
    if image.size > max_size:
        raise ValidationError("The maximum file size that can be uploaded is 5MB.")


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128)


class ProfileUpdateForm(forms.Form):
    fields = ['first_name', 'last_name', 'organization_name', 'location', 'linkedin_url', 'picture']
