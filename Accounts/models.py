from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
