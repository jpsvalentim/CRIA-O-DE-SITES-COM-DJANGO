from django.shortcuts import render
from django.http import HttpResponse

#create you views here.

# Create your views here.
def index(request):
    return HttpResponse("Olá, esse é o meu primeiro site")