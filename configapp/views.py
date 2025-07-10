from django.shortcuts import render

from django.http import HttpResponse

def salom_django(request):
    l=[]
    for i in range(10):
        l.append(i)
    return HttpResponse(l)