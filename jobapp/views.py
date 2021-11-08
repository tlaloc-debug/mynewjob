from django.shortcuts import render
from .models import Nursing, Welding, Driving, Development

# Create your views here.

def index(request):

    # text = {'title': "hola", 'read': "aqui programando con django"}
    nursing = Nursing.objects.all()
    welding = Welding.objects.all()
    driving = Driving.objects.all()
    development = Development.objects.all()
    print(nursing)
    print(welding)
    print(driving)
    print(development)
    context = {
        'nursing': nursing,
        'welding': welding,
        'driving': driving,
        'development': development,
    }
    return render(request, 'index.html', context)

def details(request, slug):

    position = Nursing.objects.filter(slug = slug).union(Welding.objects.filter(slug = slug)).union(Driving.objects.filter(slug = slug)).union(Development.objects.filter(slug = slug))
    print(position)
    context = {
        'position': position,
    }
    return render(request, 'details.html', context)
