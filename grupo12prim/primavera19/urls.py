from django.urls import path
from .views import * 

urlpatterns = [
	path('', index, name ='index'),
	path('inputs/', inputs, name='inputs'),
	path('inicio/', inicio, name='inicio'),
	path('contacto/', contacto, name='contacto'),
	path("mostrar_resultado", recuperar, name='mostrar_resultado'),
	path("mostrar_resultado2", recuperar2, name='mostrar_resultado2'),
	path("mostrar_resultado3", recuperar3, name='mostrar_resultado3'),
	path("mostrar_resultado4", recuperar4, name='mostrar_resultado4'),
]