from django.db import models

# Create your models here.
class Student(models.Model):
    suid = models.IntegerField()
    sname = models.CharField(max_length=70)
    smail = models.EmailField(max_length=70)
    spass = models.CharField(max_length=70)