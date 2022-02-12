from django.contrib import admin
from .models import student

@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display=['Name','Roll_no','City']
