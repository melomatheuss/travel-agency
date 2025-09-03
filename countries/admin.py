from django.contrib import admin
from .models import Country

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "cca2", "region", "subregion", "capital", "population")
    search_fields = ("name", "cca2", "region", "subregion", "capital")
    list_filter = ("region", "subregion")