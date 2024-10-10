from modeltranslation.translator import translator, TranslationOptions, register
from .models import OfferModel, ProblemModel, FAQModel


@register(OfferModel)
class OfferTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(ProblemModel)
class ProblemTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(FAQModel)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')
