from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from accounts.models import SigEpUser

class SigEpUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name',)
    list_filter = ('is_staff',)
    fieldsets = (
            (None, {'fields': ('email', 'password',)}),
            ('Personal Info', {'fields': ('first_name', 'last_name',)}),
            ('Permissions', {'fields': ('is_staff',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name'),
         }),
    )
    filter_horizontal = ()
    ordering = ('email',)

admin.site.register(SigEpUser, SigEpUserAdmin)
admin.site.unregister(Group)
