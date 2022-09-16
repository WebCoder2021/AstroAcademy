from django.db import models
from users.models import CustomUser
from ckeditor.fields import RichTextField
# Create your models here.
class Master(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = RichTextField()
    image = models.ImageField(upload_to='images/master')