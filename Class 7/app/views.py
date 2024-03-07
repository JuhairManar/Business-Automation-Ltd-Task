from django.shortcuts import render
from .tables import *
from .models import *
# Create your views here.
# def people(request):
#     people = PersonTable()
#     return render(request, "index.html", {'people': people})

# def person_list(request):
#     people = Person.objects.all()
#     return render(request, 'yijira.html', {'people': people})

def person_list(request):
    people = Person.objects.all()
    return render(request, 'yijira.html', {'people': people})