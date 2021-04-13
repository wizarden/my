from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):

    return HttpResponse("1")


def list_izd(request):

    return render(request, 'list_izd.html', locals())


#    ups = Up.objects.all()

#    izds = Izd.objects.all()








#    return render(request, 'et.html', {"izds": izds, "ups": ups})
