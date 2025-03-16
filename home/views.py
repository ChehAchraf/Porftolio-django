from django.shortcuts import render
from .models import PersonalInfo, TechnichalExpertise, Technology, Project , ProjectDetail , DevelopmentStage , Challenges
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
    project_detail = ProjectDetail.objects.get(project=project)
    criteria_list = project_detail.criteria.all()
    DevStage = project_detail.stages.all()
    chanllenges = project_detail.challenges.all()
    return render(request, 'single-project.html', {'project': project,"pd" : project_detail,'criteria_list': criteria_list , "devstage" : DevStage , "ch" : chanllenges})
