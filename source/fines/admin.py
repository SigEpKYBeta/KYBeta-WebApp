from django.contrib import admin
from .models import Fine


@admin.register(Fine)
class FineAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'reason',)
