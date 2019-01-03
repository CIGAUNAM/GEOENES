from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize
from django.views.generic import View
from . models import *
from . forms import *
from matplotlib.colors import LinearSegmentedColormap
import matplotlib

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


            print(colormap)

            self.context['self']['colormap'] = colormap
            self.context['self']['campo'] = campo
        except:
            pass
        return render(request, self.template_name, self.context)

class StyleImage(View):
    def get(self, request, pk):
        obj = ColorMap.objects.get(pk=pk)
        objser = serialize('json', ColorMap.objects.filter(pk=pk))
        return HttpResponse(objser)
