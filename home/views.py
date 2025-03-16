from django.shortcuts import render
from .models import PersonalInfo, TechnichalExpertise, Technology, Project
# Create your views here.

def home(request):
    personal_info = PersonalInfo.objects.get(id=1)
    front_end_technologies = TechnichalExpertise.objects.filter(category='front-end')
    back_end_technologies = TechnichalExpertise.objects.filter(category='back-end')
    technology = Technology.objects.all()
    project = Project.objects.all()
    return render(request, 'home.html' , {'ashraf':personal_info,'front_end_technologies':front_end_technologies,'back_end_technologies':back_end_technologies,'technology':technology,'project':project})


def single_project(request,id):
    project = Project.objects.get(id=id)
    return render(request, 'single-project.html', {'project': project})
