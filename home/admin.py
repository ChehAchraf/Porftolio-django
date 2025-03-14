from django.contrib import admin
from .models import PersonalInfo, TechnichalExpertise, Technology, Project

# Register your models here.
admin.site.register(PersonalInfo)
admin.site.register(TechnichalExpertise)
admin.site.register(Technology)
admin.site.register(Project)
