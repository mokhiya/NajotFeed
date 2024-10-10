from django.shortcuts import render, redirect
from django.conf import settings
from django.utils import translation
from django.utils.translation import get_language, get_language_info

from feedback_offer.models import FAQModel


def home_page_view(request):
    faqs = FAQModel.objects.all()
    context = {
        'faqs': faqs,
    }
    return render(request, 'index.html', context)


def problems_page_view(request):
    return render(request, template_name='main/forms/offer/offer-form.html')


def offers_page_view(request):
    return render(request, template_name='main/offers/offer.html')


def comments_page_view(request):
    return render(request, template_name='main/offers/offer.html')


def profile_page_view(request):
    return render(request, template_name='main/profile/profile.html')


def comment_page_view(request):
    return render(request, template_name='main/comments/comment.html')
