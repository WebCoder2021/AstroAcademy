from django.db import models
from ckeditor.fields import RichTextField
from users.models import CustomUser
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='events')
    content = RichTextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, verbose_name="Slug")

    def __str__(self):
        return self.title

class PostCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def posts_count(self):
        num = Post.objects.filter(category=self.id).count()
        return num
    def __str__(self):
        return self.name
class PostTag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='events')
    content = RichTextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(PostTag)
    created = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, verbose_name="Slug")

    def comments(self):
        comment = PostComment.objects.filter(post__slug=self.slug)
        return comment

    def __str__(self):
        return self.title

class PostComment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    content = models.TextField()
    def __str__(self):
        return self.content