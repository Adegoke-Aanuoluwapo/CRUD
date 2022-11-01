from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bravo, Welcome to my site")