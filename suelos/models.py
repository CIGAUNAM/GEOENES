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

class Organizacion(models.Model):
    organizacion_nombre = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.organizacion_nombre

class Empresa(models.Model):
    empresa_nombre = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.empresa_nombre


class Secretaria(models.Model):
    secretaria_nombre = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.secretaria_nombre

class Pueblo(models.Model):
    pueblo_nombre = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.pueblo_nombre

class ClaseRoca(models.Model):
    claseroca_nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.claseroca_nombre


class Periodico(models.Model):
    periodico_nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.periodico_nombre



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
    # data = JSONField()

class Nota(models.Model):
    titulo_nota = models.CharField(max_length=254)
    cuerpo_nota = models.TextField()
    periodico = models.ForeignKey(Periodico, on_delete=models.PROTECT)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return "{} : {}".format(self.titulo_nota, self.periodico)


class Conflicto(models.Model):
    tipo_conflicto = models.CharField(
        max_length=30,
        choices=(
            ('', '-------'), ('AGRICOLA', 'Agricola'), ('BIOTECNOLOGICO', 'Biotecnológico'), ('CARRETERO', 'Carretero'),
            ('ENERGETICO', 'Energético'), ('FORESTAL', 'Forestal'), ('HIDRICO', 'Hídrico'), ('MINERO', 'Minero'),
            ('PESQUERO', 'Pesquero'), ('RESIDUOS', 'Residuos peligrosos y rellenos sanitarios'), ('TURISTICO', 'Turístico'),
            ('URBANO', 'Urbano')))
    entidad_id = models.IntegerField()
    municipio_id = models.IntegerField()
    entidad = models.CharField(max_length=60)
    municipio = models.CharField(max_length=150)
    cabecera = models.CharField(max_length=150)
    localidad = models.CharField(max_length=150)
    total_poblacion = models.IntegerField(null=True, blank=True)
    clave = models.IntegerField()
    fecha = models.DateField()
    organizaciones = models.ManyToManyField(Organizacion, blank=True)
    empresas = models.ManyToManyField(Empresa, blank=True)
    secretaria = models.CharField(max_length=250, null=True, blank=True)
    pueblo_origen = models.ManyToManyField(Pueblo, blank=True)
    notas = models.ManyToManyField(Nota, blank=True)
    personas = models.IntegerField(null=True, blank=True)
    intereses = models.CharField(max_length=254, null=True, blank=True)
    anotaciones_adicionales = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.clave

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