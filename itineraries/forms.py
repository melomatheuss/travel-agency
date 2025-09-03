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
            "start_date": forms.DateInput(
                format='%d/%m/%Y',
                attrs={"type": "date", "class": "w-full border px-3 py-2 rounded"}
            ),
            "end_date": forms.DateInput(
                format='%d/%m/%Y',
                attrs={"type": "date", "class": "w-full border px-3 py-2 rounded"}
            ),
            "title": forms.TextInput(attrs={"class": "w-full border px-3 py-2 rounded"}),
            "country": forms.Select(attrs={"class": "w-full border px-3 py-2 rounded"}),
            "description": forms.Textarea(attrs={"rows": 4, "class": "w-full border px-3 py-2 rounded"}),
            "price": forms.NumberInput(attrs={"class": "w-full border px-3 py-2 rounded"}),
            "image": forms.FileInput(attrs={"class": "w-full border px-3 py-2 rounded"}),
        }