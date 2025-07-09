from django.contrib import admin
from .models import ShortLink

# Register your models here.

@admin.register(ShortLink)
class ShortLinkAdmin(admin.ModelAdmin):
    list_display = ('slug', 'target_url', 'description')
    search_fields = ('slug', 'target_url')