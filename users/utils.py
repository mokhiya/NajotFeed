from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from users.form import ProfileUpdateForm
from users.models import UserModel


@login_required(login_url='users:login')
def profile_page_view(request):
    user = User.objects.filter(username=request.user.username).first()
    profile = UserModel.objects.filter(user__username=request.user.username).first()

    if request.method == 'POST':
        print(request.POST)
        form = ProfileUpdateForm(request.POST)
        if form.is_valid():
            User.objects.filter(pk=request.user.pk).update(
                username=request.POST['username'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
            )
            UserModel.objects.filter(user__pk=request.user.pk).update(
                organization_name=request.POST['organization_name'],
                location=request.POST['location'],
                linkedin_url=request.POST['linkedin_url'],
            )

    context = {
        'user': user,
        'profile': profile,
    }
    return render(request, 'main/profile/profile.html', context)
