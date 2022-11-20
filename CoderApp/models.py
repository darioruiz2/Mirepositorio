from django.db import models

class Familia(models.Model):
    Nombre = models.CharField(max_length=50)
    Edad = models.IntegerField()
    Fecha_nacimiento = models.CharField(max_length = 50)
    

    

