from django.db import models

# Create your models here.
class Student(models.Model):
    suid=models.IntegerField()
    sname=models.CharField(max_length=70)
    smail=models.EmailField()
    spass=models.CharField(max_length=70)

# this will help to see the specific table section name to see the which of the table of it
    def __str__(self):
        # return self.suid
        return str(self.suid) #integer must need to convert as string.