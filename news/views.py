from django.shortcuts import render

# Create your views here.
def events (request):
    return render(request,'news/events.html')
def event_detail (request):
    return render(request,'news/event-details.html')
def blog (request):
    return render(request,'news/blog-home.html')
def blog_detail (request):
    return render(request,'news/blog-single.html')