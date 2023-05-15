from django.shortcuts import render
from django.db.models.functions import *
from django.db.models import Q
# Create your views here.

from app.models import *

def display_topic(request):
    lot=Topic.objects.all()
    d={'topic':lot}
    return render(request,'display_topic.html',context=d)

def display_webpage(request):
    low=Webpage.objects.all()
    low=Webpage.objects.all().order_by('-name')
    low=Webpage.objects.all().order_by(Length('name').desc())
    low=Webpage.objects.exclude(name='dhoni')
    low=Webpage.objects.filter(name__startswith='d')
    low=Webpage.objects.filter(name__endswith='j')
    low=Webpage.objects.filter(name__in=('dhoni','raj'))
    low=Webpage.objects.filter(name__contains='a')
    low=Webpage.objects.filter(name__regex='[a-zA-Z]{5}')
    low=Webpage.objects.filter(Q(topic_name='cricket') & Q(name='dhoni'))

    d={'webpage':low}
    return render(request,'display_webpage.html',d)


def update_webpage(request):
    Webpage.objects.filter(name='dhoni').update(url='http://dhoni.in')
    TO=Topic.objects.get_or_create(topic_name='cricket') [0]
    TO.save()
    Webpage.objects.update_or_create(name='RUSSELL',defaults={'topic_name':TO,'url':'http://RUSSELL.com'})
    Webpage.objects.filter(name='RAHUL').update(url='http://rahul.com')
    Webpage.objects.filter(name='RAHUL').delete()
    Webpage.objects.filter(name='RUSSELL').update(url='http://russell.in')
    TO=Topic.objects.get_or_create(topic_name='KOKO') [0]
    TO.save()
    Webpage.objects.update_or_create(name='RAM',defaults={'topic_name':TO,'url':'http://suraj.com'})
    Webpage.objects.filter(name='SAM').delete()
    Webpage.objects.filter(name='RAM').delete()

    d={'webpage':Webpage.objects.all()}
    return render(request,'display_webpage.html',d)


def display_accessrecord(request):
    loa=AccessRecord.objects.all()
    loa=AccessRecord.objects.filter(date__gt='2015-05-15')
    loa=AccessRecord.objects.filter(date__lt='2012-08-15')
    loa=AccessRecord.objects.filter(date__gte='2016-08-20')
    loa=AccessRecord.objects.filter(date__lte='2015-06-18')
    loa=AccessRecord.objects.filter(date__year='2018')
    loa=AccessRecord.objects.filter(date__day='20')
    loa=AccessRecord.objects.filter(date__month__lt='08')
    d={'accessrecord':loa}
    return render(request,'display_accessrecord.html',d)