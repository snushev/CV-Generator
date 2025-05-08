from django.db import models

# Create your models here.

class Profile(models.Model):
    
    image = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    summary = models.TextField(max_length=2000)
    degree = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    previous_work = models.CharField(max_length=50)
    skills = models.TextField(max_length=2000)
    

    def __str__(self):
        return self.name
