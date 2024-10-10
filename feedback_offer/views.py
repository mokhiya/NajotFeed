from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings
from django.utils import translation
from django.utils.translation import get_language, get_language_info

from feedback_offer.form import ProblemForm, OfferForm
from feedback_offer.models import FAQModel
from users.models import TeamMemberModel


def home_page_view(request):
    faqs = FAQModel.objects.all()
    team_members = TeamMemberModel.objects.all()
    context = {
        'faqs': faqs,
        'team_members': team_members,
    }

    return render(request, 'index.html', context)


def problems_page_view(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your request has been submitted!")
            return redirect('feedback_offer:problems')
    else:
        form = ProblemForm()
    return render(request, template_name='main/forms/offer/offer-form.html', context={'form': form})


@login_required
def offer_submit(request):
    if request.method == 'POST':
        form = OfferForm(request.POST, request.FILES)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.user = request.user
            offer.save()
            return redirect('feedback_offer:index')
    else:
        form = OfferForm()

    return render(request, 'main/forms/offer/offer-form.html', {'form': form})


def offers_page_view(request):
    return render(request, template_name='main/offers/offer.html')


def comments_page_view(request):
    return render(request, template_name='main/offers/offer.html')


def profile_page_view(request):
    return render(request, template_name='main/profile/profile.html')


def comment_page_view(request):
    return render(request, template_name='main/comments/comment.html')
