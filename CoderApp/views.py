from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse
from django.template import loader

def familia(request):
    
    familiarcero = Familia(Nombre = "Dario",Edad = 24, Fecha_nacimiento = "05/08/1998")
    familiaruno = Familia(Nombre = "Pedro",Edad = 23, Fecha_nacimiento = "05/08/1999")
    familiardos = Familia(Nombre = "Fernando",Edad = 22, Fecha_nacimiento = "05/08/2000")
    
    familiarcero.save()
    familiaruno.save()
    familiardos.save()
    
    diccionario = {"familiar1": familiarcero, "familiar2":familiaruno, "familiar3": familiardos}
    
    
    
    plantilla = loader.get_template("plantillita.html")
    
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)
    
    