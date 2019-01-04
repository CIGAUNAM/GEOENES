from django.contrib.gis.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from django.contrib.postgres.fields import JSONField

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


class TipoRoca(models.Model):
    tiporoca_nombre = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.tiporoca_nombre


class TipoSuelo(models.Model):
    tiposuelo_nombre = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.tiposuelo_nombre


class UsoSuelo(models.Model):
    usosuelo_nombre = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.usosuelo_nombre


class Suelo(models.Model):
    entidad = models.CharField(max_length=100)
    municipio = models.CharField(max_length=120)
    clase_roca = models.CharField(max_length=50)
    tipo_roca = models.CharField(max_length=120)
    tipo_suelo = models.CharField(max_length=120)
    uso_suelo = models.CharField(max_length=120)
    area = models.IntegerField(blank=True, null=True)
    geom = models.MultiPolygonField()
    data = JSONField()


class PaletaColor(models.Model):
    nombre_paleta = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_paleta


class ColorMap(models.Model):
    colormap_nombre = models.CharField(max_length=100, unique=True)
    colormap_paleta = models.ForeignKey(PaletaColor, on_delete=models.PROTECT)
    colormap_importstring = models.CharField(max_length=190)
    colormap_continuous = models.ImageField(null=True, blank=True)
    colormap_discrete = models.ImageField(null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.colormap_paleta, self.colormap_nombre )


class SuelosIndexPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full')
    ]