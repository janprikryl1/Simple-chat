from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import safe

from .models import Message
from django.core import serializers

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def upload(request):
    if request.is_ajax():
        msg = request.POST.get('msg')
        user = request.POST.get('user')
        Message(message=msg, user=user).save()
        return JsonResponse({"Status": "OK"})
    else:
        return JsonResponse({"Status":"error"})

def load(request):
    user = ""
    for i in range(0, len(Message.objects.all())):
        user += f'{Message.objects.all()[i].user}&&&{Message.objects.all()[i].message}&&&{Message.objects.all()[i].date_time}@@@'

    d = request.POST.get('datas')
    if request.is_ajax():
        if d != user:
            return JsonResponse({"data":user})
        else:
            return JsonResponse({"data":"nothong"})

def l(request):
    return render(request, "l.html", {"a":Message.objects.all()})