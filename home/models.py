from django.db import models

# Create your models here.


class PersonalInfo(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    bio = models.TextField()
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.name