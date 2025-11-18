from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ej1/", views.ejercicio1, name="ej1"),
    path("ej2/", views.ejercicio2, name="ej2"),
    path("ej3/", views.ejercicio3, name="ej3"),
    path("ej4/<int:anio>/", views.ejercicio4, name="ej4"),
    path("ej5/<str:centro_nombre>/", views.ejercicio5, name="ej5"),
    path("ej6/<str:veterinario_nombre>/<str:fabricante>/<str:refugio_nombre>/", views.ejercicio6, name="ej6"),
]
