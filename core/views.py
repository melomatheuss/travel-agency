from django.shortcuts import render
from countries.models import Country
from itineraries.models import Itinerary

def home_view(request):
    total_countries = Country.objects.count()
    total_itineraries = Itinerary.objects.count()

    featured_countries = Country.objects.all()[:6]

    recent_itineraries = Itinerary.objects.order_by('-created_at')[:3]

    return render(request, 'home.html', {
        'total_countries': total_countries,
        'total_itineraries': total_itineraries,
        'featured_countries': featured_countries,
        'recent_itineraries': recent_itineraries,
    })