from django.db import models


class Multimedia_Principal(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.titulo
    
class Frase_Principal(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

class Tipos_De_Comida_Imagen_Por_Producto(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
    
class Comidas_Imagen_Por_Producto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/')
    Pertenece_A = models.ForeignKey(Tipos_De_Comida_Imagen_Por_Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Tipos_De_Comida_Unica_Imagen(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        return self.titulo

class Comidas_Unica_Imagen(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.CharField(max_length=100)
    Pertenece_A = models.ForeignKey(Tipos_De_Comida_Unica_Imagen, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
class Promociones(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        return self.titulo

class Comentarios(models.Model):
    NUMBER_CHOICES = (
        ('1', '1'),
        ('1.5', '1.5'),
        ('2', '2'),
        ('2.5', '2.5'),
        ('3', '3'),
        ('3.5', '3.5'),
        ('4', '4'),
        ('4.5', '4.5'),
        ('5', '5'),
    )
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    calificacion = models.CharField(max_length=100, choices=NUMBER_CHOICES)
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        return self.titulo

class Mapa(models.Model):
    titulo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/')
    latitud = models.CharField(max_length=100)
    longitud = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class Contacto(models.Model):
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.telefono
    
class Tipo_de_Bebida(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        return self.titulo

class Bebidas(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.CharField(max_length=100)
    pertenece_A = models.ForeignKey(Tipo_de_Bebida, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Novedades(models.Model):
    imagen = models.ImageField(upload_to='imagenes/')
