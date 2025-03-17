from os import name
from django.db import models
from ckeditor.fields import RichTextField

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
    
class Criteria(models.Model):
    criteria = models.CharField(max_length=200)
    details  = models.CharField(max_length=200)

    def __str__(self):
        return self.criteria

class ProjectDetail(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    criteria = models.ManyToManyField(Criteria , related_name='project_details')
    detail = models.CharField(max_length=200)
    project_overview = RichTextField()
    key_features = RichTextField()
    PojTechnology = models.ManyToManyField(Technology, related_name='project_technologies')
    diagram_file = models.FileField(upload_to='diagram/')
    what_ilearned = models.TextField()
    def __str__(self):
        return f"Details of {self.project.name}"

class DevelopmentStage(models.Model):
    project = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE, related_name='stages')  
    title = models.CharField(max_length=255)  
    week = models.PositiveIntegerField()  
    description = models.TextField() 

    def __str__(self):
        return f"{self.project.detail} - Week {self.week}: {self.title}"

class Challenges(models.Model):
    project = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE, related_name='challenges')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.project.project.name} - {self.title}"


class ProjectTechnology(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    usage_description = models.TextField()  
    class Meta:
        unique_together = ("project", "technology")
    def __str__(self):
        return f"{self.technology.name} in {self.project.name}"
