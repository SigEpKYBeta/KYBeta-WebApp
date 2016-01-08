from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from accounts.models import User


def make_active_brother(modeladmin, request, queryset):
    group = Group.objects.get(name='Active Brother')
    for user in queryset:
        user.groups.add(group)
    ModelAdmin.message_user(self=modeladmin, request=request,
                            message='Selected users were added to the '
                                    'Active Brother group')
make_active_brother.short_description = 'Make selected member Active Brother'


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name',)
    list_filter = ('is_superuser',)
    fieldsets = (
            (None, {'fields': ('email', 'password',)}),
            ('Personal Info', {'fields': ('first_name',
                                          'last_name',)}),
            ('Permissions', {'fields': ('is_superuser', 'groups',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name'),
         }),
    )
    filter_horizontal = (['groups'])
    ordering = ('email',)
    actions = [make_active_brother]

admin.site.register(User, CustomUserAdmin)
