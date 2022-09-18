from django.db import models

# Create your models here.
class AboutUsComment(models.Model):
    name = models.CharField(max_length=250)
    content = models.TextField()
    star1 = models.BooleanField(default=False)
    star2 = models.BooleanField(default=False)
    star3 = models.BooleanField(default=False)
    star4 = models.BooleanField(default=False)
    star5 = models.BooleanField(default=False)

    def __str__(self):
        return self.name
class AboutInfoTab(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.title

class Gallary(models.Model):
    image = models.ImageField(upload_to='gallary')
    order = models.IntegerField()
    col = models.PositiveSmallIntegerField()

class Messages(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name