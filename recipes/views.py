from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Cleiton',
        })

def contato(request):
    return HttpResponse("contato")

def sobre(request):
    return HttpResponse("sobre")
