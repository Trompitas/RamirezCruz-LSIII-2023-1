from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirige al usuario a la página de dashboard si el inicio de sesión es exitoso
        else:
            messages.error(request, 'Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.')
            pass

    return render(request, 'index.html')

