from django.shortcuts import render
from django.views.generic import View
from . models import *
# Create your views here.

class SuelosIndex(View):
    template_name = 'suelos/suelos_index.html'
    context = {'self': {'title': 'Suelos de México'}}

    def get(self, request):
        return render(request, self.template_name, self.context)

class PolygonSLD(View):
    template_name = 'suelos/sld/polygon.sld'
    context = {'self': {'titles': 'Suelos de México'}}

    def get(self, request):
        title = request.GET['title']
        b = request.GET['color']
        print(title)
        print(title.get('color'))
        print(b)
        return render(request, self.template_name, self.context)
