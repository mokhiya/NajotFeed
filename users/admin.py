from django.contrib import admin

from users.models import TeamMemberModel, UserModel


@admin.register(TeamMemberModel)
class TeamMemberModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role', 'description', 'picture', 'created_at')
    list_filter = ('role', 'created_at')
    search_fields = ('first_name', 'last_name', 'role', 'description')


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'password', 'email', 'picture', 'created_at')
    list_filter = ('password', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'password')

