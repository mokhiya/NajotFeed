from modeltranslation.translator import translator, TranslationOptions, register
from .models import UserModel, TeamMemberModel


@register(UserModel)
class OfferTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'location', 'organization_name')


@register(TeamMemberModel)
class ProblemTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'role', 'description')
