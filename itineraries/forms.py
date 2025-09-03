from django import forms
from .models import Itinerary

class ItineraryForm(forms.ModelForm):
    class Meta:
        model = Itinerary
        fields = ["title", "country", "start_date", "end_date", "description", "price", "image"]
        labels = {
            "title": "Título",
            "country": "País",
            "start_date": "Data de Início",
            "end_date": "Data de Término",
            "description": "Descrição",
            "price": "Preço",
            "image": "Imagem",
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }