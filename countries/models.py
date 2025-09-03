from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=150)
    cca2 = models.CharField(max_length=2, unique=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    subregion = models.CharField(max_length=100, blank=True, null=True)
    capital = models.CharField(max_length=150, blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)
    flag_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.cca2})"