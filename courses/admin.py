from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Course_outline)
admin.site.register(CourseComment)
admin.site.register(WeekDay)
admin.site.register(Schedule)

class CourseAdmin(admin.ModelAdmin):
    list_display = ["id","name"]
    list_display_links = ('id',"name")
    prepopulated_fields = {'slug':('name',),}
    save_as = True
    group_fieldsets = True
admin.site.register(Course,CourseAdmin)
