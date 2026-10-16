from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    contexto = {
        'titulo': 'página de mi juego de GODOT!',
        'mensaje': 'acá se subirán las noticias del juego',
        'usuario': 'visitante'
    }
    return render(request, 'index.html', contexto)

# Create your views here.
