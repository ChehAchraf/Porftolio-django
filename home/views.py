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


def all_project(request):
    project = Project.objects.all()
    technology = Technology.objects.all()
    return render(request, 'all_project.html',{'projects' : project, "techs" : technology})

def filter_projects(request):
    selected_techs = request.GET.getlist('techs')
    sort_by = request.GET.get('sort', 'newest')  

    print(f"Selected technologies: {selected_techs}")
    if sort_by == 'newest':
        projects = Project.objects.all().order_by('-id')  
    elif sort_by == 'oldest':
        projects = Project.objects.all().order_by('id')  
    elif sort_by == 'a-z':
        projects = Project.objects.all().order_by('name') 
    elif sort_by == 'z-a':
        projects = Project.objects.all().order_by('-name')  
    else:
        projects = Project.objects.all()
    # Always get all projects first
    projects = Project.objects.all()
    print(f"Total projects before filtering: {projects.count()}")
    
    # Only filter if technologies are selected
    if selected_techs:
        projects = projects.filter(technology__name__in=selected_techs).distinct()
        print(f"Projects after filtering: {projects.count()}")
    
    # Make sure we're passing the queryset with the right context name
    context = {"projects": projects}
    print(f"Context being passed to template: {context}")
    
    return render(request, "partials/project_list.html", context)