from django.shortcuts import render
from django.views.generic import View
from . models import *
# Create your views here.

class SuelosIndex(View):
    template_name = 'suelos/suelos_index.html'
    context = {'self': {'title': 'Suelos de México'}}

    def get(self, request):
        return render(request, self.template_name, self.context)
