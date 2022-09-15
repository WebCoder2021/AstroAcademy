from django.urls import path
from .views import *
urlpatterns = [
    path('', courses, name='courses'),
    path('detail', courses_detail, name='courses_detail'),
]