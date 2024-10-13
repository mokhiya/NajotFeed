from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.utils import translation
from django.utils.translation import get_language, get_language_info

from feedback_offer.form import ProblemForm, OfferForm
from feedback_offer.models import FAQModel, OfferModel, ProblemModel
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
            messages.success(request, "Your request has been submitted successfully!")
            return redirect('feedback_offer:problems')
    else:
        form = ProblemForm()
    return render(request, template_name='main/forms/offer/offer-form.html', context={'form': form})


@login_required(login_url='users:login')
def submit_offer_view(request):
    if request.method == 'POST':
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.user = request.user
            offer.save()
            messages.success(request, 'Your offer has been submitted successfully.')
            return redirect('feedback_offer:problems')
        else:
            messages.error(request, 'There was an error submitting your offer.')
    else:
        form = OfferForm()

    return render(request, 'main/forms/offer/offer-form.html', {'form': form})


def offers_page_view(request):
    selected_category = request.GET.get('category', 'offers')

    my_offers = OfferModel.objects.filter(user=request.user)
    demands = ProblemModel.objects.all()
    offers = OfferModel.objects.all()

    context = {
        'offers': offers,
        'demands': demands,
        'my_offers': my_offers,
        'selected_category': selected_category,
    }
    print("Selected Category:", selected_category)
    print("My Offers:", my_offers)
    print("Demands:", demands)
    print("User:", request.user)
    return render(request, template_name='main/offers/offer.html', context=context)


def offer_detail_view(request, offer_id):
    offer = get_object_or_404(OfferModel, id=offer_id)
    offer.count_views()

    context = {
        'offer': offer,
    }
    return render(request, 'main/offers/offer.html', context=context)


def comments_page_view(request):
    return render(request, template_name='main/offers/offer.html')


def comment_page_view(request):
    return render(request, template_name='main/comments/comment.html')
