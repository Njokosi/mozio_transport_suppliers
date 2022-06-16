from django.contrib import admin
from .models import Provider, ServiceArea

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name', 'email', 'currency')
    

class ServiceAreaAdmin(admin.ModelAdmin):
    list_display = ('provider', 'name', 'price')
    search_fields = ('provider', 'name', 'price')

admin.site.register(Provider, ProviderAdmin)
admin.site.register(ServiceArea, ServiceAreaAdmin)