from django.contrib import admin
from . models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display=['id','title','description']

admin.site.register(Project,ProjectAdmin)

