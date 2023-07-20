from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Multimedia_Principal, Frase_Principal, Tipos_De_Comida_Imagen_Por_Producto, Comidas_Imagen_Por_Producto, Tipos_De_Comida_Unica_Imagen, Comidas_Unica_Imagen, Promociones, Comentarios, Mapa, Contacto, Tipo_de_Bebida, Bebidas, Novedades

admin.site.register(Multimedia_Principal)
admin.site.register(Frase_Principal)
admin.site.register(Tipos_De_Comida_Imagen_Por_Producto)
admin.site.register(Comidas_Imagen_Por_Producto)
admin.site.register(Tipos_De_Comida_Unica_Imagen)
admin.site.register(Comidas_Unica_Imagen)
admin.site.register(Promociones)
admin.site.register(Comentarios)
admin.site.register(Mapa)
admin.site.register(Contacto)
admin.site.register(Tipo_de_Bebida)
admin.site.register(Bebidas)
admin.site.register(Novedades)