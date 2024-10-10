from django import forms
from .models import ProblemModel, OfferModel


class ProblemForm(forms.ModelForm):
    class Meta:
        model = ProblemModel
        fields = ['title', 'description']


class OfferForm(forms.ModelForm):
    class Meta:
        model = OfferModel
        fields = ['title', 'description', 'picture']
