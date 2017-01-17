from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("WOW THIS ACTUALLY WORKS !!!")



# Create your views here.
