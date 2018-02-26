from django.contrib import admin

# Register your models here.
from .models import Pelicula
from .models import Sala
from .models import Cartelera
from .models import Venta
from .models import Imagen

class AdminPelicula(admin.ModelAdmin):
	list_display= ["nombre","estado","duracion"]
	class Meta:
		model=Pelicula
class AdminSala(admin.ModelAdmin):
	list_display= ["id_sala","nombre","capacidad"]
	class Meta:
		model=Sala
class AdminCartelera(admin.ModelAdmin):
	list_display= ["id_cartelera","id_pelicula","id_sala","fecha","hora","valor"]
	class Meta:
		model=Cartelera
class AdminVenta(admin.ModelAdmin):
	list_display= ["id_ventas","nombre","cedula","tarjeta","fecha","hora","numero_boletos","fecha_compra","total_pagar"]
	class Meta:
		model=Venta
class AdminImagen(admin.ModelAdmin):
	list_display= ["id_imagen","url"]
	class Meta:
		model=Imagen

admin.site.register(Pelicula,AdminPelicula)
admin.site.register(Sala,AdminSala)
admin.site.register(Cartelera,AdminCartelera)
admin.site.register(Venta,AdminVenta)
admin.site.register(Imagen,AdminImagen)
