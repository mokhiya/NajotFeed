from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

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


@login_required(login_url='users:login')
def offers_page_view(request):
    selected_category = request.GET.get('category', 'offers')
    search_query = request.GET.get('search', '')

    my_offers = OfferModel.objects.filter(user=request.user)
    demands = ProblemModel.objects.all()
    offers = OfferModel.objects.all()

    if search_query:
        offers = offers.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )
        demands = demands.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )

    context = {
        'offers': offers if selected_category == 'offers' else None,
        'demands': demands if selected_category == 'demands' else None,
        'my_offers': my_offers if selected_category == 'my_offers' else None,
        'selected_category': selected_category,
        'search_query': search_query,
    }

    return render(request, 'main/offers/offer.html', context)


def offer_detail_view(request, offer_id):
    offer = get_object_or_404(OfferModel, id=offer_id)
    offer.count_views()

    context = {
        'offer': offer,
    }
    return render(request, 'main/offers/offer.html', context=context)


def demand_detail_view(request, demand_id):
    demand = get_object_or_404(ProblemModel, id=demand_id)
    demand.count_views()

    context = {
        'demand': demand,
    }
    return render(request, 'main/offers/offer.html', context=context)


def comments_page_view(request):
    return render(request, template_name='main/offers/offer.html')


def comment_page_view(request):
    return render(request, template_name='main/comments/comment.html')
