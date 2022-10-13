from django.http import HttpResponse
from django.shortcuts import render
from AppF1.models import Pilotos,Constructores,Circuitos
from AppF1.forms import PilotosFormulario, ConstructoresFormulario, CircuitosFormulario


def inicio(request):
    
    return render (request,"inicio.html")


def crear_pilotos(request):
    piloto = Pilotos(nombre = "Max Verstappen", nacionalidad= "Países Bajos", fecha_nacimiento="1997-4-5")
    piloto.save()
    dict_pilotos={"piloto_1": piloto,
                  
    }
    return render (request,"pilotos.html",dict_pilotos)


def crear_constructores(request):
    
    constructor = Constructores (nombre="Red Bull", nacionalidad= "Austria",email="redbull@constructores.com")
    constructor.save()
    dict_constructores={"constructor_1":constructor,}
    return render (request,"constructores.html",dict_constructores)


def crear_circuitos(request):
    circuito= Circuitos(nombre="Monzza", país="Italia",año_primer_carrera="1970-5-5")
    circuito.save()
    dict_circuitos={"circuito_1":circuito}
    return render (request,"circuitos.html",dict_circuitos)


def procesar_formulario_pilotos(request):
    if request.method != "POST":
        mi_formulario = PilotosFormulario()
    else:
        mi_formulario = PilotosFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            piloto = Pilotos(nombre=informacion["nombre"], nacionalidad=informacion["nacionalidad"],fecha_nacimiento=informacion["fecha_nacimiento"])
            piloto.save()
            return render(request, "inicio.html")

    contexto = {"formulario_pilotos": mi_formulario}

    return render(request, "formulario_pilotos.html", contexto)


def procesar_formulario_constructores(request):
    if request.method != "POST":
        mi_formulario = ConstructoresFormulario()
    else:
        mi_formulario = ConstructoresFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            constructor = Constructores(nombre=informacion["nombre"], nacionalidad=informacion["nacionalidad"],email=informacion["email"])
            constructor.save()
            return render(request, "inicio.html")

    contexto = {"formulario_constructores": mi_formulario}

    return render(request, "formulario_constructores.html", contexto)


def procesar_formulario_circuitos(request):
    if request.method != "POST":
        mi_formulario = CircuitosFormulario()
    else:
        mi_formulario = CircuitosFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            circuitos = Circuitos(nombre=informacion["nombre"], país=informacion["país"],año_primer_carrera=informacion["año_primer_carrera"])
            circuitos.save()
            return render(request, "inicio.html")

    contexto = {"formulario_circuitos": mi_formulario}

    return render(request, "formulario_circuitos.html", contexto)

def busqueda(request):
    return render(request, "busqueda.html")

def buscar_piloto(request):

    if not request.GET["nombre"]:
        return HttpResponse("No enviaste datos")
    else:
        nombre_a_buscar = request.GET["nombre"]
        piloto = Pilotos.objects.filter(nombre=nombre_a_buscar)

        contexto = {"nombre": nombre_a_buscar, "piloto_encontrado": piloto}

        return render(request, "resultado_busqueda.html", contexto)