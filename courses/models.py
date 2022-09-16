from django.db import models
from ckeditor.fields import RichTextField
from users.models import CustomUser
from master.models import Master
# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=250, unique=True)
    sub_title = models.CharField(max_length=500)
    image = models.ImageField(upload_to ='images/courses/')
    sale = models.CharField(max_length=100)
    objective = RichTextField()
    eligibility = RichTextField()
    slug = models.SlugField(max_length=500,unique=True)
    order = models.IntegerField(null=True, blank=True, default=0)
    trainer = models.ForeignKey(Master,on_delete=models.CASCADE, null=True)
    def course_outlines(self):
        outlines = Course_outline.objects.filter(course__slug=self.slug)
        return outlines
    def comments(self):
        comment = CourseComment.objects.filter(course__slug=self.slug)
        return comment
    def schedule(self):
        comment = Schedule.objects.filter(course__slug=self.slug)
        return comment
    def __str__(self):
        return self.name

class Course_outline(models.Model):
    order = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/courses/outline')
    def __str__(self):
        return self.title


class CourseComment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    content = models.TextField()
    def __str__(self):
        return self.content

class WeekDay(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Schedule(models.Model):
    time = models.TimeField()
    group_number = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    order = models.IntegerField()
    week = models.ForeignKey(WeekDay, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.name



