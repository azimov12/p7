from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def summer(request):
    return HttpResponse('It is Summer')

def winter(request):
    return HttpResponse('It is Winter')

def autumn(request):
    return HttpResponse('It is Autumn')

def spring(request):
    return HttpResponse('It is Spring')