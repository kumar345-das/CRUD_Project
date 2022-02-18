from django.contrib import admin
from testapp.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['First_name','Last_name','Gender','Email']
admin.site.register(Student,StudentAdmin)