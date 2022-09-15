from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
class EventAdmin(admin.ModelAdmin):
    list_display = ["id","title"]
    list_display_links = ('id',"title")
    prepopulated_fields = {'slug':('title',),}
    save_as = True
    group_fieldsets = True
admin.site.register(Event,EventAdmin)