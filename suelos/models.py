from django.contrib.gis.db import models

# Create your models here.

class Entidad(models.Model):
    entidad_nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.entidad_nombre


class Municipio(models.Model):
    municipio_nombre = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.municipio_nombre


class ClaseRoca(models.Model):
    claseroca_nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.claseroca_nombre




class Suelo(models.Model):
    entidad = models.CharField(max_length=100)
    municipio = models.CharField(max_length=120)
    clase_roca = models.CharField(max_length=50)
    tipo_roca = models.CharField(max_length=120)
    tipo_suelo = models.CharField(max_length=120)
    uso_suelo = models.CharField(max_length=120)
    area = models.IntegerField()
    geom = models.MultiPolygonField()
