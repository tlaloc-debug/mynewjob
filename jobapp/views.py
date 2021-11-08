from django.shortcuts import render
from .models import Nursing, Welding, Driving, Development
from django.core.mail import EmailMessage

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


def yourSend(request):
    if request.method == "POST":
        your_position = request.POST['your_position']
        your_name = request.POST['your_name']
        your_email = request.POST['your_email']
        your_phone = request.POST['your_phone']
        
        message_object = {
            'Cantidate_Position': your_position,
            'Candidate_Name' : your_name,
            'Candidate_Email' : your_email,
            'Candidate_Phone' : your_phone
        }
        new_message = str(message_object)
        apply_email = EmailMessage(
            "Hi, I'd like to apply for a position", new_message, 'no-reply@merakidesigns.ca', ['pelondinho@hotmail.com'])
        if request.FILES:
            your_file = request.FILES['your_file']
            apply_email.attach(filename=your_file.name, mimetype=your_file.content_type, content=your_file.read())
        apply_email.send()
        # send_mail(subject='A cool subject', message=new_message, from_email='no-reply@merakidesigns.ca', recipient_list=['pelondinho@hotmail.com'])

    return render(request, "sendemail.html")