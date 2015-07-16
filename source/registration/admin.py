from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from registration.models import SigEpUser

class SigEpUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name',)
    list_filter = ('is_staff',)
    filter_horizontal = ()
    ordering = ('email',)

admin.site.register(SigEpUser, SigEpUserAdmin)
admin.site.unregister(Group)