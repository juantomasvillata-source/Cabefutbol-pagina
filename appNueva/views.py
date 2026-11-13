from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    contexto = {
        'titulo': 'página de mi juego de GODOT!',
        'mensaje': 'acá se subirán las noticias del juego',
        'usuario': 'visitante'
    }
    return render(request, 'index.html', contexto)

def index2(request):
    contexto = {
        'titulo': 'página de mi juego de GODOT!',
        'mensaje': 'acá se subirán las noticias del juego',
        'usuario': 'visitante'
    }
    return render(request, 'App1/index2.html', contexto)

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def vista_login(request):
    if request.method == 'POST':
        # Recoges los datos del formulario (nota que en tu HTML el input se llama 'correo')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')

        user = authenticate(request, username=correo, password=contrasena)

        if user is not None:
            login (request, user)
            return redirect('index')  # Redirige a la página de inicio después del login exitoso
        else:
            return render(request, 'login.html', {'error': 'Correo o contraseña incorrectos.'})
        # Aquí validarías al usuario con tu lógica o con authenticate() de Django
        # user = authenticate(request, username=correo, password=contrasena)
        
        # Si el login es exitoso:
        # login(request, user)
        return redirect('index') # 'index' debe ser el nombre de la URL configurada en tu urls.py
        
    return render(request, 'login.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages # <-- 1. Importa el sistema de mensajes

def vista_signup(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        
        if User.objects.filter(username=correo).exists():
            messages.error(request, 'El correo ya está registrado.')
            return redirect('signup')
        
        # Creamos el usuario
        usuario = User.objects.create_user(
            username=correo, 
            email=correo, 
            password=contrasena,
            first_name=nombre,
            last_name=apellido
        )
        usuario.save()
        
        # 2. Agregamos el mensaje de éxito
        messages.success(request, '¡Cuenta creada!')
        
        # 3. Redirigimos al login
        return redirect('login')
        
    return render(request, 'signup.html')
# Create your views here.
