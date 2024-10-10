from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from users.form import RegistrationForm, LoginForm, ProfileUpdateForm
from users.models import UserModel, TeamMemberModel
from users.token import email_verification_token


def verify_email(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)
    if user is not None and email_verification_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Account activated')
        return redirect(reverse_lazy('users:login'))
    else:
        messages.error(request, 'The verification link is invalid.')
        return redirect(reverse_lazy('users:login'))


def send_email_verification(request, user):
    token = email_verification_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    current_site = get_current_site(request)
    verification_url = reverse('users:verify_email', kwargs={'uidb64': uid, 'token': token})
    full_url = f"http://{current_site.domain}/{verification_url}"

    text_content = render_to_string(
        'main/auth/register/verify-email.html',
        {
            'user': user,
            'full_url': full_url,
        }
    )

    message = EmailMultiAlternatives(
        subject='Email Verification',
        body=text_content,
        to=[user.email],
        from_email=settings.EMAIL_HOST_USER
    )
    message.attach_alternative(text_content, 'text/html')
    message.send()


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()
            send_email_verification(request, user)
            return redirect(reverse_lazy('users:login'))
        else:
            errors = form.errors
            return render(request, 'main/auth/register/register.html', {"errors": errors})
    return render(request, template_name='main/auth/register/register.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(request.user)
                return redirect("/")
            else:
                messages.error(request, 'Invalid username or password')
                return render(request, template_name='main/auth/login/login.html')
    else:
        return render(request, 'main/auth/login/login.html')


def team_member_view(request):
    team_members = TeamMemberModel.objects.all()
    print(team_members)
    context = {
        'team_members': team_members
    }
    return render(request, 'index.html', context)

# # Chronically saving user data between django-user and my user model
# @receiver(post_save, sender=User)
# def create_user_model(sender, instance, created, **kwargs):
#     if created:
#         UserModel.objects.create(
#             user=instance,
#             first_name=instance.first_name,
#             last_name=instance.last_name,
#             email=instance.email,
#             username=instance.username,
#             password=instance.password
#         )
#
#
# @receiver(post_save, sender=User)
# def save_user_model(sender, instance, **kwargs):
#     instance.usermodel.save()
#
#
# @login_required
# def update_profile(request):
#     user_model = request.user.usermodel
#     if request.method == 'POST':
#         form = ProfileUpdateForm(request.POST, request.FILES, instance=user_model)
#         if form.is_valid():
#             form.save()
#             return redirect('feedback_offer:profile')
#     else:
#         form = ProfileUpdateForm(instance=user_model)
#
#     return render(request, 'main/profile/profile.html', {'form': form})
