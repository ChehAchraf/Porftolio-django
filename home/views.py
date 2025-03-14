from django.shortcuts import render
from .models import PersonalInfo, TechnichalExpertise, Technology, Project
# Create your views here.

def home(request):
    personal_info = PersonalInfo.objects.get(id=1)
    technichal_expertise = TechnichalExpertise.objects.all()
    technology = Technology.objects.all()
    project = Project.objects.all()
    return render(request, 'home.html' , {'ashraf':personal_info,'technology':technology})
