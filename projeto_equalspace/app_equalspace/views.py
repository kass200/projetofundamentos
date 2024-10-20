from django.shortcuts import render

def home(request):
    return render(request, 'usuarios/home.html')

def noticias(request):
    return render(request, 'noticias.html')