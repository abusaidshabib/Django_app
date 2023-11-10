from django.contrib import admin
from .models import Student
# Register your models here.

# best practice
@admin.register(Student)
# help watch the table details on name
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','suid', 'sname', 'semail')

# not good practice
# admin.site.register(Student, StudentAdmin)