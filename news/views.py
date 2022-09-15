from django.shortcuts import render
from .models import *
# Create your views here.
def events (request):
    events = Event.objects.all()
    category = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'events': events,
        'category': category,
        'tags': tags,
    }
    return render(request,'news/events.html',context)
def event_detail(request,slug):
    context ={}
    event = Event.objects.filter(slug=slug).first()
    context['event'] = event
    return render(request,'news/event-details.html',context)
def blog (request):
    return render(request,'news/blog-home.html')
def blog_detail (request):
    return render(request,'news/blog-single.html')