from django.contrib import admin
from . import models

admin.site.register(models.Refugio)
admin.site.register(models.Centro)
admin.site.register(models.Veterinario)
admin.site.register(models.Vacuna)
admin.site.register(models.Animal)
admin.site.register(models.AnimalVacunas)
admin.site.register(models.RevisionVeterinaria)
