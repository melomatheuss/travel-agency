from django.contrib import admin
from .models import Itinerary

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ("title", "country", "start_date", "end_date", "price")
    list_filter = ("country", "start_date", "end_date")
    search_fields = ("title", "description", "country__name")    
