from django.shortcuts import render, get_object_or_404
from .models import Country

def country_list(request):
    search = request.GET.get("search", "")
    region = request.GET.get("region", "")
    ordering = request.GET.get("ordering", "name")

    countries = Country.objects.all()

    if search:
        countries = countries.filter(name__icontains=search)

    if region:
        countries = countries.filter(region__iexact=region)

    if ordering:
        countries = countries.order_by(ordering)

    return render(request, "countries/country_list.html", {"countries": countries})

def country_detail(request, cca2):
    country = get_object_or_404(Country, cca2=cca2)
    itineraries = country.itineraries.all()
    return render(request, "countries/country_detail.html", 
                    {
                        "country": country, 
                        "itineraries": itineraries
                    }
                )