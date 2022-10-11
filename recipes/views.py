from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(requests):
    return HttpResponse('HOME')


def contato(requests):
    return HttpResponse('CONTATO')


def sobre(requests):
    return HttpResponse('SOBRE')
