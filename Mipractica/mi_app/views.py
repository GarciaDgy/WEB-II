# views.py
from django.http import JsonResponse
from django.shortcuts import render
from .models import Estado, Municipio

def cargar_formulario(request):
    estados = Estado.objects.all()
    return render(request, 'formulario.html', {'estados': estados})

def cargar_municipios(request):
    estado_id = request.GET.get('estado_id')
    municipios = Municipio.objects.filter(estado_id=estado_id).order_by('nombre')
    municipios_data = [{'id': municipio.id, 'nombre': municipio.nombre} for municipio in municipios]
    return JsonResponse(municipios_data, safe=False)
