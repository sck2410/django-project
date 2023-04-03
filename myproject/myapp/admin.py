from django.contrib import admin
from myapp.models import department, student

# Register your models here.
admin.site.register(department)
admin.site.register(student)