from django.shortcuts import render
from django.http import HttpResponse

def salom_func1(request):
    d={"Model": "Bmw","Color":"Black"}
    javob = ""
    for i, j in d.items():
        javob += f"{i}: {j}<br>"

    a = {"Ismi": "Abdulaziz", "Familiyasi": "Mutalov"}
    ja = ""
    for i, j in a.items():
        ja += f"{i}:{j}\n"

    javob+=ja
    return HttpResponse(javob)


