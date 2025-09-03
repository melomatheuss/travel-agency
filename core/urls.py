from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from countries.views import country_list, country_detail
from itineraries.views import itinerary_list, itinerary_detail,itinerary_create, itinerary_update

urlpatterns = [
    path('admin/', admin.site.urls),

    path('countries/', country_list, name='country_list'),
    path('countries/<str:cca2>/', country_detail, name='country_detail'),

    path('itineraries/', itinerary_list, name='itinerary_list'),
    path('itineraries/<int:id>/', itinerary_detail, name='itinerary_detail'),
    path('itineraries/add/', itinerary_create, name='itinerary_create'),
    path('itineraries/<int:id>/edit/', itinerary_update, name='itinerary_update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)