from django.contrib import admin
from .models import Provider

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name', 'email', 'currency')
    


admin.site.register(Provider, ProviderAdmin)