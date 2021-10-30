from django.shortcuts import render
from .models import Nursing, Welding, Driving, Development

# Create your views here.

def index(request):

    # text = {'title': "hola", 'read': "aqui programando con django"}
    nursing = Nursing.objects.all()
    print(nursing)
    context = {
        'nursing': nursing,
    }
    return render(request, 'index.html', context)

def details(request, slug):

    context = {'name': slug,}

    return render(request, 'details.html', {'context': context})
