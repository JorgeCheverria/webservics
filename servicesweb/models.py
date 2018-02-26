from django.db import models

# Create your models here.
class Pelicula(models.Model):
	id_pelicula=models.AutoField(primary_key=True)
	nombre=models.TextField()
	estado=models.TextField()
	duracion=models.TextField()
	def __str__(self):
		return self.nombre

class Sala(models.Model):
	id_sala=models.AutoField(primary_key=True)
	nombre=models.TextField()
	capacidad=models.TextField()
	def __str__(self):
		return self.nombre

class Cartelera(models.Model):
	id_cartelera=models.AutoField(primary_key=True)
	id_pelicula=models.ForeignKey(Pelicula,null=True,on_delete=models.CASCADE)
	id_sala=models.ForeignKey(Sala,null=True,on_delete=models.CASCADE)
	fecha=models.TextField()
	hora=models.TextField()
	valor=models.DecimalField(max_digits=3,decimal_places=1)
	def __str__(self):
		return self.fecha


class Venta(models.Model):
	id_ventas=models.AutoField(primary_key=True)
	nombre=models.TextField()
	cedula=models.TextField()
	tarjeta=models.TextField()	
	id_cartelera=models.ForeignKey(Cartelera,null=True,on_delete=models.CASCADE)
	fecha=models.TextField()
	hora=models.TextField()
	numero_boletos=models.TextField()
	fecha_compra=models.DateTimeField(auto_now_add=True)
	total_pagar=models.DecimalField(max_digits=3,decimal_places=1)
class Imagen(models.Model):
	id_imagen=models.AutoField(primary_key=True)
	url=models.TextField()

