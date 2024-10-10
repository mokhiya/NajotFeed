from django.contrib import admin

from feedback_offer.models import OfferModel, ProblemModel, FAQModel
from users.admin import MyTranslation


@admin.register(OfferModel)
class OfferModelAdmin(MyTranslation):
    list_display = ('title', 'description', 'user', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('title', 'description')


@admin.register(ProblemModel)
class ProblemModelAdmin(MyTranslation):
    list_display = ('title', 'description', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)


@admin.register(FAQModel)
class FAQModelAdmin(MyTranslation):
    list_display = ('question', 'answer', 'created_at')
    search_fields = ('question', 'answer')
    list_filter = ('created_at',)


