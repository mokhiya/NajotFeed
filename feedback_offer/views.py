from django.shortcuts import render


def home_page_view(request):
    return render(request, 'index.html')


def problems_page_view(request):
    return render(request, template_name='main/forms/offer/offer-form.html')


def offers_page_view(request):
    return render(request, template_name='main/offers/offer.html')


def comments_page_view(request):
    return render(request, template_name='main/offers/offer.html')
