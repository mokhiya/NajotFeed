from django.contrib import admin

from feedback_offer.models import OfferModel, ProblemModel, FAQModel


@admin.register(OfferModel)
class OfferModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'user', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('title', 'description')


@admin.register(ProblemModel)
class ProblemModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)


@admin.register(FAQModel)
class FAQModelAdmin(admin.ModelAdmin):
    list_display = ('question', 'name', 'created_at')
    search_fields = ('question', 'name')
    list_filter = ('created_at',)


