from django.shortcuts import render
from django.db.models import Avg
from .models import *

def index(request):
    return render(request, "refugio/index.html")

def ejercicio1(request):
    animales = Animal.objects.select_related("centro", "centro__refugio").prefetch_related("vacunas").filter(
        nombre__icontains="Max",
        centro__refugio__nombre__icontains="Animales Felices"
    )
    return render(request, "refugio/ej1.html", {"animales": animales, "titulo": "Ejercicio 1"})

def ejercicio2(request):
    animales = Animal.objects.select_related("centro").prefetch_related("vacunas", "revisionveterinaria_set").filter(
        vacunas__fabricante__icontains="Zoetis",
        revisionveterinaria__puntuacion_salud__gt=80
    )[:3]
    return render(request, "refugio/ej2.html", {"animales": animales, "titulo": "Ejercicio 2"})

def ejercicio3(request):
    animales = Animal.objects.filter(animalvacunas__isnull=True).order_by("-edad_estimada")
    return render(request, "refugio/ej3.html", {"animales": animales, "titulo": "Ejercicio 3"})

def ejercicio4(request, anio):
    refugios = Refugio.objects.filter(
        centro__animal__revisionveterinaria__fecha__year=anio
    ).order_by("-centro__animal__revisionveterinaria__puntuacion_salud").distinct()
    return render(request, "refugio/ej4.html", {"refugios": refugios, "anio": anio})

def ejercicio5(request, centro_nombre):
    animales = Animal.objects.filter(
        centro__nombre__icontains=centro_nombre
    ).annotate(media=Avg("revisionveterinaria__puntuacion_salud")).filter(media__lt=100)  
    return render(request, "refugio/ej5.html", {"animales": animales, "centro": centro_nombre})

def ejercicio6(request, veterinario_nombre, fabricante, refugio_nombre):
    revision = RevisionVeterinaria.objects.select_related("animal", "veterinario", "animal__centro__refugio").filter(
        veterinario__nombre__icontains=veterinario_nombre,
        animal__vacunas__fabricante__icontains=fabricante,
        animal__centro__refugio__nombre__icontains=refugio_nombre
    ).order_by("-fecha").first()
    return render(request, "refugio/ej6.html", {"revision": revision})
