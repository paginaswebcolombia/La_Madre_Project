from django.shortcuts import render
from django.core.cache import cache
from .models import (Multimedia_Principal, Frase_Principal, 
    Tipos_De_Comida_Imagen_Por_Producto, Comidas_Imagen_Por_Producto, 
    Tipos_De_Comida_Unica_Imagen, Comidas_Unica_Imagen, Promociones, 
    Comentarios, Mapa, Contacto, Tipo_de_Bebida, Bebidas, Novedades)
import json
from django.http import HttpResponse

def data_api(request):
    json_data = cache.get('data_api_cache')
    if not json_data:
        modelo1_data = Multimedia_Principal.objects.all().values()
        modelo2_data = Frase_Principal.objects.all().values()
        modelo3_data = Tipos_De_Comida_Imagen_Por_Producto.objects.all().values()
        modelo4_data = Comidas_Imagen_Por_Producto.objects.all().values()
        modelo5_data = Tipos_De_Comida_Unica_Imagen.objects.all().values()
        modelo6_data = Comidas_Unica_Imagen.objects.all().values()
        modelo7_data = Promociones.objects.all().values()
        modelo8_data = Comentarios.objects.all().values()
        modelo9_data = Mapa.objects.all().values()
        modelo10_data = Contacto.objects.all().values()
        modelo11_data = Tipo_de_Bebida.objects.all().values()
        modelo12_data = Bebidas.objects.all().values()
        modelo13_data = Novedades.objects.all().values()

        data = {
            'Multimedia_Principal': list(modelo1_data),
            'Frase_Principal': list(modelo2_data),
            'Tipos_De_Comida_Imagen_Por_Producto': list(modelo3_data),
            'Comidas_Imagen_Por_Producto': list(modelo4_data),
            'Tipos_De_Comida_Unica_Imagen': list(modelo5_data),
            'Comidas_Unica_Imagen': list(modelo6_data),
            'Promociones': list(modelo7_data),
            'Comentarios': list(modelo8_data),
            'Mapa': list(modelo9_data),
            'Contacto': list(modelo10_data),
            'Tipo_De_Bebida': list(modelo11_data),
            'Bebidas': list(modelo12_data),
            'Novedades': list(modelo13_data)
        }
        
        json_data = json.dumps(data)
        cache.set('data_api_cache', json_data, timeout=3600)  # Almacena en caché los datos durante 1 hora

    return HttpResponse(json_data, content_type='application/json')


