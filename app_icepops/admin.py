from django.contrib import admin
from app_icepops.models import Icepop

# Register your models here.

class IcepopAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_premium', 'promo_end_at']
    search_fields = ['title']
    list_filter = ['is_premium']


admin.site.register(Icepop, IcepopAdmin)