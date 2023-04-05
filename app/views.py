from django.shortcuts import render

# Create your views here.

from app.models import *

def display_topic(request):
    lot=Topic.objects.all()
    d={'topic':lot}
    return render(request,'display_topic.html',context=d)

def display_webpage(request):
    low=Webpage.objects.all()
    d={'webpage':low}
    return render(request,'display_webpage.html',d)

def display_accessrecord(request):
    loa=AccessRecord.objects.all()
    d={'accessrecord':loa}
    return render(request,'display_accessrecord.html',d)