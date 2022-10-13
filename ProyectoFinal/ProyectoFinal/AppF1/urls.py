from django.urls import path
from AppF1.views import inicio, crear_pilotos, crear_constructores, crear_circuitos,procesar_formulario_pilotos,procesar_formulario_constructores,procesar_formulario_circuitos,buscar_piloto,busqueda


urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('pilotos/', crear_pilotos, name="pilotos"),
    path('constructores/', crear_constructores, name="constructores"),
    path('circuitos/', crear_circuitos,name="circuitos"),
    path('formulario_pilotos/', procesar_formulario_pilotos,name="formulario_pilotos"),
    path('formulario_constructores/', procesar_formulario_constructores,name="formulario_constructores"),
    path('formulario_circuitos/', procesar_formulario_circuitos,name="formulario_circuitos"),
    path("busqueda/", busqueda, name="busqueda"),
    path("buscar_piloto/", buscar_piloto),
]