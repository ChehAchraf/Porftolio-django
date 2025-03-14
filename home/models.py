from os import name
from django.db import models

# Create your models here.

CHOICES = (
    ('front-end', 'Front-End'),
    ('back-end', 'Back-End'),
)

class PersonalInfo(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    bio = models.TextField()
    long_bio = models.TextField()
    years_of_experience = models.CharField(max_length=200)
    completed_projects = models.CharField(max_length=200)
    awards = models.CharField(max_length=200)
    happy_clients = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    cv = models.FileField(upload_to='cv/')

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=200)
    icon_url = models.CharField(max_length=200)   

    def __str__(self):
        return self.name

class TechnichalExpertise(models.Model):
    name = models.CharField(max_length=200)
    percent = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=CHOICES)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.ManyToManyField(Technology) 
    image = models.ImageField(upload_to='project/') 
    live_link = models.CharField(max_length=200)
    github_link = models.CharField(max_length=200)

    def __str__(self):
        return self.name