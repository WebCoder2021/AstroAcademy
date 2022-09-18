from django.db import models
from courses.models import Course, OurGroup
from users.models import CustomUser
# Create your models here.
class CourseGroup(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    group = models.OneToOneField(OurGroup, on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True, blank=True)
    register_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.course.name) + ' ' + str(self.group.name)

class Student(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    parent_phone = models.CharField(max_length=100, null=True, blank=True)
    course_groups = models.ManyToManyField(CourseGroup)

    def __str__(self):
        return str(self.user.phone) + ' - ' + str(self.user.first_name) + ' ' + str(self.user.last_name)
