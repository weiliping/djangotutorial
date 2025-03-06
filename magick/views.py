from django.http import HttpResponse
from django.shortcuts import render
from .models import Person

# Create your views here.

def index(request):
    p = Person.objects.create(first_name="John1", last_name="Doe1")
    p.save()
    persons = Person.objects.all()
    context = {
        'persons': persons
    }
    return render(request, 'index.html', context=context)