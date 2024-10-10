from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.utils import validate_image_size


class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="usermodel")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    organization_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    linkedin_url = models.URLField(unique=True, blank=True, null=True)
    picture = models.ImageField(upload_to='users', validators=[validate_image_size], blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class TeamMemberModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to='team_pictures/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _('TeamMember')
        verbose_name_plural = _('TeamMembers')
