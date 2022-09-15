from django.shortcuts import render

# Create your views here.
def courses (request):
    return render(request,'courses/courses.html')
def courses_detail (request):
    return render(request,'courses/course-details.html')