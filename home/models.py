from os import name
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

CHOICES = (
    ('front-end', 'Front-End'),
    ('back-end', 'Back-End'),
    )

PROJECT_CATEGORIES = (
    ('web', 'Web Development'),
    ('mobile', 'Mobile Apps'),
    ('ui', 'UI/UX Design'),
    ('backend', 'Backend'),
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
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    live_link = models.URLField(max_length=200, default='none')
    github_link = models.URLField(max_length=200, default='none')
    technology = models.ManyToManyField(Technology)
    category = models.CharField(max_length=20, choices=PROJECT_CATEGORIES, default='web')
    year = models.IntegerField(default=2023)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProjectGallery(models.Model):
    project = models.ForeignKey(Project, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_gallery/')
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']

    def __str__(self):
        return f"{self.project.name} - {self.title or 'Untitled'}"

class ProjectDetail(models.Model):
    project = models.OneToOneField('Project', on_delete=models.CASCADE, related_name='detail')
    project_overview = RichTextField()
    key_features = RichTextField()
    what_ilearned = models.TextField(blank=True, null=True)
    diagram_file = models.FileField(upload_to='diagram/', blank=True, null=True)
    PojTechnology = models.ManyToManyField(Technology, related_name='project_technologies', blank=True)

    def __str__(self):
        return f"Details for {self.project.name}"

class ProjectMetric(models.Model):
    project_detail = models.ForeignKey(ProjectDetail, related_name='metrics', on_delete=models.CASCADE)
    metric_name = models.CharField(max_length=200)
    metric_value = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.project_detail.project.name} - {self.metric_name}"

    class Meta:
        verbose_name = "Project Metric"
        verbose_name_plural = "Project Metrics"

class DevelopmentStage(models.Model):
    project = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE, related_name='stages')  
    title = models.CharField(max_length=200)
    description = models.TextField()
    week = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.project.project.name} - {self.title}"

class Challenges(models.Model):
    project = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE, related_name='challenges')  
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.project.project.name} - {self.title}"

    class Meta:
        verbose_name_plural = "Challenges"

class ProjectTechnology(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    usage_description = models.TextField()  
    class Meta:
        unique_together = ("project", "technology")
    def __str__(self):
        return f"{self.technology.name} in {self.project.name}"
