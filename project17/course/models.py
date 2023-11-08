from django.db import models

# Create your models here.
class Student(models.Model):
    suid=models.IntegerField()
    suname = models.CharField(max_length=70)
    stuemail=models.EmailField(max_length=70)
    stupass=models.CharField(max_length=70)
    comment=models.CharField(max_length=500, default="not available")