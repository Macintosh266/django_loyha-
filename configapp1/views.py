from django.shortcuts import render
from django.http import HttpResponse

def salom_func(request):
    d={"Soat":17,"Minute":20}
    d=d.items()
    return HttpResponse(d)