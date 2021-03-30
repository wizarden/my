from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):

    return HttpResponse("1")



#    ups = Up.objects.all()

#    izds = Izd.objects.all()








#    return render(request, 'et.html', {"izds": izds, "ups": ups})
