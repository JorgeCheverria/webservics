"""WebServices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from servicesweb import views
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('webservices/compras/(?P<id>\d+)/$', views.wsCompra),
    path('webservices/peliculas', views.wsPeliculas),
    path('webservices/salas', views.wsSalas),
    path('webservices/carteleras', views.wsCarteleras),
    path('webservices/ventas', views.wsVentas),
    url(r'^webservices/imagenes/(?P<url>\d+)/$', views.wsImagen),
    url(r'^webservices/compras/(?P<id_c>\d+)/(?P<fecha>\d+)/(?P<hora>\d+)/(?P<numero_boletos>\d+)/(?P<fecha_compra>\d+)/(?P<total_pagar>\d+)/(?P<nombre>\d+)/(?P<cedula>\d+)/(?P<tarjeta>\d+)/$', views.wsCompra)

]
