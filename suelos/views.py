from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize
from django.views.generic import View
from . models import *
from . forms import *
from matplotlib.colors import LinearSegmentedColormap
import matplotlib
import urllib
from palettable.cartocolors.diverging import *
from palettable.cartocolors.sequential import *
from palettable.cartocolors.qualitative import *



# Create your views here.

class SuelosIndex(View):
    template_name = 'suelos/suelos_index.html'
    # form_class = SueloForm
    context = {'self': {'title': 'Suelos de México'}, 'form': SueloForm, 'colormap_form': ColorMapForm}

    def get(self, request):
        return render(request, self.template_name, self.context)

class PolygonSLD(View):
    template_name = 'suelos/sld/polygon.sld'
    context = {'self': {'titles': 'Suelos de México'}}

    def get(self, request):
        try:
            colormap = request.GET['colormap']
            campo = request.GET['campo']
            try:
                cql = request.GET['cql']
                cql = urllib.parse.unquote(cql, 'latin')
                print(cql)
            except:
                pass
            camposet = Suelo.objects.values_list(campo, flat=True).distinct().order_by(campo)
            cmap = ColorMap.objects.get(pk=colormap)

            cm = LinearSegmentedColormap.from_list(cmap.colormap_nombre, eval(cmap.colormap_nombre + ".mpl_colors"), N=camposet.count())
            colors = []

            for i in range(cm.N):
                rgb = cm(i)[:3]
                colors.append(matplotlib.colors.rgb2hex(rgb))

            print(colors)

            print(list(camposet))

            colorcampo = list(zip(camposet, colors))






            self.context['self']['colors'] = colors
            self.context['self']['campo'] = campo
            self.context['self']['camposet'] = camposet
            self.context['colorcampo'] = colorcampo
        except Exception as e:
            print(e)
        return render(request, self.template_name, self.context)

class StyleImage(View):
    def get(self, request, pk):
        obj = ColorMap.objects.get(pk=pk)
        objser = serialize('json', ColorMap.objects.filter(pk=pk))
        return HttpResponse(objser)
