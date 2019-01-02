from wagtail.contrib.modeladmin.options import (ModelAdmin, ModelAdminGroup, modeladmin_register)
from . models import *

class EntidadAdmin(ModelAdmin):
    model = Entidad
    menu_label = 'Entidades'  # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse'  # change as required
    list_display = ('entidad_nombre', )
    list_filter = ('entidad_nombre', )
    search_fields = ('entidad_nombre',)

class MunicipioAdmin(ModelAdmin):
    model = Municipio
    menu_label = 'Municipios'  # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse'  # change as required
    list_display = ('municipio_nombre', )
    list_filter = ('municipio_nombre', )
    search_fields = ('municipio_nombre',)

class ClaseRocaAdmin(ModelAdmin):
    model = ClaseRoca
    menu_label = 'Clases de Roca'  # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse'  # change as required
    list_display = ('claseroca_nombre', )
    list_filter = ('claseroca_nombre', )
    search_fields = ('claseroca_nombre',)


class TipoRocaAdmin(ModelAdmin):
    model = TipoRoca
    menu_label = 'Tipos de Roca'  # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse'  # change as required
    list_display = ('tiporoca_nombre', )
    list_filter = ('tiporoca_nombre', )
    search_fields = ('tiporoca_nombre',)

class TipoSueloAdmin(ModelAdmin):
    model = TipoSuelo
    menu_label = 'Tipos de Suelo'  # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse'  # change as required
    list_display = ('tiposuelo_nombre', )
    list_filter = ('tiposuelo_nombre', )
    search_fields = ('tiposuelo_nombre',)

class UsoSueloAdmin(ModelAdmin):
    model = UsoSuelo
    menu_label = 'Usos de Suelo'  # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse'  # change as required
    list_display = ('usosuelo_nombre', )
    list_filter = ('usosuelo_nombre', )
    search_fields = ('usosuelo_nombre',)

class SueloAdmin(ModelAdmin):
    model = Suelo
    menu_label = 'Suelos'  # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse'  # change as required
    list_display = ('entidad', 'municipio', 'clase_roca',)
    list_filter = ('entidad', 'municipio', 'clase_roca', )
    search_fields = ('entidad', 'municipio', 'clase_roca', )

class PaletaColorAdmin(ModelAdmin):
    model = PaletaColor
    menu_label = 'Paletas de color'  # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse'  # change as required
    list_display = ('nombre_paleta', )
    list_filter = ('nombre_paleta', )
    search_fields = ('nombre_paleta',)


class ColorMapAdmin(ModelAdmin):
    model = ColorMap
    menu_label = 'Mapas de color'  # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full-inverse'  # change as required
    list_display = ('colormap_nombre', 'colormap_paleta', 'colormap_continuous', 'colormap_discrete')
    list_filter = ('colormap_nombre', 'colormap_paleta')
    search_fields = ('colormap_nombre', 'colormap_paleta')


modeladmin_register(EntidadAdmin)
modeladmin_register(MunicipioAdmin)
modeladmin_register(ClaseRocaAdmin)
modeladmin_register(TipoRocaAdmin)
modeladmin_register(TipoSueloAdmin)
modeladmin_register(UsoSueloAdmin)
modeladmin_register(SueloAdmin)
modeladmin_register(PaletaColorAdmin)
modeladmin_register(ColorMapAdmin)