from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from countries.views import country_list, country_detail
from itineraries.views import itinerary_list, itinerary_detail

urlpatterns = [
    path('admin/', admin.site.urls),

    path('countries/', country_list, name='country_list'),
    path('countries/<str:cca2>/', country_detail, name='country_detail'),

    path('itineraries/', itinerary_list, name='itinerary_list'),
    path('itineraries/<int:id>/', itinerary_detail, name='itinerary_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)