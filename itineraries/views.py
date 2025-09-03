from django.shortcuts import render, get_object_or_404
from .models import Itinerary
from countries.models import Country

def itinerary_list(request):
    country_code = request.GET.get("country", "")
    start_date = request.GET.get("start_date", "")
    end_date = request.GET.get("end_date", "")

    itineraries = Itinerary.objects.all()

    if country_code:
        itineraries = itineraries.filter(country__cca2=country_code)

    if start_date:
        itineraries = itineraries.filter(start_date__gte=start_date)

    if end_date:
        itineraries = itineraries.filter(end_date__lte=end_date)
    
    countries = Country.objects.all()

    return render(request, "itineraries/itinerary_list.html", {
        "itineraries": itineraries,
        "countries": countries,
        })

def itinerary_detail(request, id):
    itinerary = get_object_or_404(Itinerary, id=id)
    return render(request, "itineraries/itinerary_detail.html", {"itinerary": itinerary})