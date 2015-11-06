from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from accounts.models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name',)
    list_filter = ('is_superuser',)
    fieldsets = (
            (None, {'fields': ('email', 'password',)}),
            ('Personal Info', {'fields': ('first_name',
                                          'last_name',
                                          'is_brother')}),
            ('Permissions', {'fields': ('is_superuser',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name'),
         }),
    )
    filter_horizontal = ()
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
