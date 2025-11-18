from django.db import models

class Refugio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    def __str__(self): return self.nombre

class Centro(models.Model):
    nombre = models.CharField(max_length=100)
    refugio = models.ForeignKey(Refugio, on_delete=models.CASCADE)
    def __str__(self): return f"{self.nombre} ({self.refugio.nombre})"

class Veterinario(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self): return self.nombre

class Vacuna(models.Model):
    nombre = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    def __str__(self): return f"{self.nombre} ({self.fabricante})"

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    edad_estimada = models.IntegerField()
    centro = models.ForeignKey(Centro, on_delete=models.CASCADE)
    vacunas = models.ManyToManyField("Vacuna", through="AnimalVacunas")
    def __str__(self): return self.nombre

class AnimalVacunas(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    vacuna = models.ForeignKey(Vacuna, on_delete=models.CASCADE)
    def __str__(self): return f"{self.animal} - {self.vacuna}"

class RevisionVeterinaria(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    puntuacion_salud = models.FloatField()
    fecha = models.DateField()
    def __str__(self): return f"{self.animal} - {self.puntuacion_salud}"
