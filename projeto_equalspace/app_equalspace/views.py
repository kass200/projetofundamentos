from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, 'usuarios/home.html')

def noticias(request):
    return render(request, 'noticias.html')

def perfil(request):
    return render(request, 'perfil.html')



def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        # Verificar se as senhas coincidem
        if password != confirm_password:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('register')

        # Criar um novo usuário
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já está registrado.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Conta criada com sucesso! Faça o login.')
            return redirect('login')  # Redirecionar para a página de login

    return render(request, 'register.html')
