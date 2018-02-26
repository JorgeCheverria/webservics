from django.shortcuts import render
from django.http import HttpResponse
#importar modelos
from servicesweb.models import Pelicula
from servicesweb.models import Sala
from servicesweb.models import Cartelera
from servicesweb.models import Venta
from servicesweb.models import Imagen
from django.core import serializers 

def index(request):
	return HttpResponse("Estamos creando nuestra view")
def wsSalas(request):
	data=serializers.serialize("json",Sala.objects.all())
	return HttpResponse(data,content_type='application/json')
def wsPeliculas(request):
	data=serializers.serialize("json",Pelicula.objects.all())
	return HttpResponse(data,content_type='application/json')
def wsCarteleras(request):
	data=serializers.serialize("json",Cartelera.objects.all())
	return HttpResponse(data,content_type='application/json')
def wsVentas(request):
	data=serializers.serialize("json",Venta.objects.all())
	return HttpResponse(data,content_type='application/json')
def wsCompra(request,id_c,fecha,hora,numero_boletos,fecha_compra,total_pagar,nombre,cedula,tarjeta):
	v=Cartelera.objects.get(id_cartelera=id_c)
	v=Venta(id_cartelera=v,nombre=nombre,cedula=cedula,tarjeta=tarjeta,fecha=fecha,hora=hora,numero_boletos=numero_boletos,fecha_compra=fecha_compra,total_pagar=total_pagar)
	v.save()
	return HttpResponse("guardado")
def wsImagen(request,url):
	i=Imagen(url=url)
	i.save()
	return HttpResponse("Guardado")