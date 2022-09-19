from django.db import models
from courses.models import Course, OurGroup
from users.models import CustomUser
# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,verbose_name="O'quvchi username")
    parent_phone = models.CharField(max_length=100, null=True, blank=True,verbose_name="Ota-ona telefon raqami")
    courses = models.ManyToManyField(OurGroup,verbose_name="O'quvchi qatnashadigan kurslar")

    def __str__(self):
        return str(self.user.phone) + ' - ' + str(self.user.first_name) + ' ' + str(self.user.last_name)
    class Meta:
        verbose_name_plural = 'O`quvchilar'
        verbose_name = 'O`quvchi'
