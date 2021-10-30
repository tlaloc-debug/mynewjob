from django.shortcuts import render
from .models import Position

# Create your views here.

def index(request):

    # text = {'title': "hola", 'read': "aqui programando con django"}
    position = Position.objects.all()
    print(position)
    context = {
        'position': position,
    }
    return render(request, 'index.html', context)

def details(request, slug):

    context = {'name': slug,}

    return render(request, 'details.html', {'context': context})
