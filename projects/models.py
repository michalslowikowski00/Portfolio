from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    date = models.TextField()
    image = models.CharField(max_length=100)


class Home(models.Model):
    image = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
