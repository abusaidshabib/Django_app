from django.db import models

# Create your models here.
class Student(models.Model):
    suid = models.IntegerField()
    sname = models.CharField(max_length=70)
    semail = models.EmailField()
    spass = models.CharField(max_length=70)

