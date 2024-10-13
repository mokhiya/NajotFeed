from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from users.models import TeamMemberModel, UserModel


class MyTranslation(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(TeamMemberModel)
class TeamMemberModelAdmin(MyTranslation):
    list_display = ('first_name', 'last_name', 'role', 'description', 'picture', 'created_at')
    list_filter = ('role', 'created_at')
    search_fields = ('first_name', 'last_name', 'role', 'description')


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('user__first_name', 'user__last_name', 'user__username', 'picture', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'user__password')
