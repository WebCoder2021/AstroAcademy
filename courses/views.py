from django.shortcuts import render
from .models import *
# Create your views here.
def courses (request):
    context = {}
    courses = Course.objects.all().order_by('order')
    context['courses'] = courses
    return render(request,'courses/courses.html',context)
def courses_detail (request,slug):
    context = {}
    course = Course.objects.filter(slug=slug).first()
    if request.method == 'POST' and request.POST.get('message',False):
        msg = CourseComment.objects.create(user=request.user, course=course,content=request.POST.get('message',False))
        msg.save()
    context['course'] = course
    context['populars'] = Course.objects.exclude(slug=slug).all()[:4]
    return render(request,'courses/course-details.html',context)