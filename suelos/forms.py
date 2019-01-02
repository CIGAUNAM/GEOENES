from django.forms import ModelMultipleChoiceField, ModelChoiceField

from .models import *
from django import forms
from django_select2.forms import Select2MultipleWidget, Select2Widget


class SueloForm(forms.Form):
    entidad = ModelMultipleChoiceField(
        queryset=Suelo.objects.values_list('entidad', flat=True).distinct().order_by('entidad'),
        widget=Select2MultipleWidget(
            attrs={'style': 'width: 100%', 'class': 'form-control pull-right'}
        )
    )
    municipio = ModelMultipleChoiceField(
        queryset=Suelo.objects.values_list('municipio', flat=True).distinct().order_by('municipio'),
        widget=Select2MultipleWidget(
            attrs={'style': 'width: 100%', 'class': 'form-control pull-right'}
        )
    )
    clase_roca = ModelMultipleChoiceField(
        queryset=Suelo.objects.values_list('clase_roca', flat=True).distinct().order_by('clase_roca'),
        widget=Select2MultipleWidget(
            attrs={'style': 'width: 100%', 'class': 'form-control pull-right'}
        )
    )
    tipo_roca = ModelMultipleChoiceField(
        queryset=Suelo.objects.values_list('tipo_roca', flat=True).distinct().order_by('tipo_roca'),
        widget=Select2MultipleWidget(
            attrs={'style': 'width: 100%', 'class': 'form-control pull-right'}
        )
    )
    tipo_suelo = ModelMultipleChoiceField(
        queryset=Suelo.objects.values_list('tipo_suelo', flat=True).distinct().order_by('tipo_suelo'),
        widget=Select2MultipleWidget(
            attrs={'style': 'width: 100%', 'class': 'form-control pull-right'}
        )
    )
    uso_suelo = ModelMultipleChoiceField(
        queryset=Suelo.objects.values_list('uso_suelo', flat=True).distinct().order_by('uso_suelo'),
        widget=Select2MultipleWidget(
            attrs={'style': 'width: 100%', 'class': 'form-control pull-right'}
        )
    )


class ColorMapForm(forms.Form):
    colormap = forms.ModelChoiceField(

        queryset=ColorMap.objects.all().order_by('colormap_nombre'),
        widget=Select2Widget(
            attrs={'style': 'width: 100%', 'class': 'form-control pull-right'}
        )
    )