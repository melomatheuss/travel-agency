import requests
from django.core.management.base import BaseCommand
from countries.models import Country

class Command(BaseCommand):
    help = "Sincroniza países a partir da API"

    def handle(self, *args, **kwargs):
        url = "https://restcountries.com/v3.1/all?fields=name,cca2,region,subregion,capital,population,flags"
        self.stdout.write("Buscando países ..")

        try:
            headers = {"User-Agent": "travel-agency-django"}
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Erro na busca de países: {e}"))
            return

        count = 0
        for item in data:
            cca2 = item.get("cca2")
            name = item.get("name", {}).get("common")
            region = item.get("region")
            subregion = item.get("subregion")
            capital = item.get("capital", [None])[0] if item.get("capital") else None
            population = item.get("population")
            flag_url = item.get("flags", {}).get("png")

            if not cca2 or not name:
                continue

            Country.objects.update_or_create(
                cca2=cca2,
                defaults={
                    "name": name,
                    "region": region,
                    "subregion": subregion,
                    "capital": capital,
                    "population": population,
                    "flag_url": flag_url,
                }
            )
            count += 1

        self.stdout.write(self.style.SUCCESS(f"{count} países sincronizados com sucesso!"))