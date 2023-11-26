from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)


# After creating model and makemigrations with migrate we can get 4 permissions will add automatically on the permission field