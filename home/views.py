from django.shortcuts import render
from .models import PersonalInfo, TechnichalExpertise, Technology, Project , ProjectDetail , DevelopmentStage , Challenges
from django.db import models
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

def home(request):
    personal_info = PersonalInfo.objects.get(id=1)
    front_end_technologies = TechnichalExpertise.objects.filter(category='front-end')
    back_end_technologies = TechnichalExpertise.objects.filter(category='back-end')
    technology = Technology.objects.all()
    project = Project.objects.all().order_by('-created_at')[:6]
    return render(request, 'home.html' , {'ashraf':personal_info,'front_end_technologies':front_end_technologies,'back_end_technologies':back_end_technologies,'technology':technology,'project':project})


def single_project(request, id):
    project = Project.objects.get(id=id)
    project_detail = ProjectDetail.objects.get(project=project)
    gallery_images = project.gallery_images.all()
    dev_stages = project_detail.stages.all()
    challenges = project_detail.challenges.all()
    context = {
        'project': project,
        'project_detail': project_detail,
        'gallery_images': gallery_images,
        'devstage': dev_stages,
        'ch': challenges,
    }
    return render(request, 'single-project.html', context)


def all_project(request):
    # Get all projects with related technologies
    projects = Project.objects.all().prefetch_related('technology')
    techs = Technology.objects.all()
    
    # Pagination
    page = request.GET.get('page', 1)
    projects_per_page = 9  # 3x3 grid
    
    # Create paginator
    paginator = Paginator(projects, projects_per_page)
    
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    
    context = {
        'projects': projects,
        'techs': techs,
        'total_projects': paginator.count,
        'total_pages': paginator.num_pages,
        'current_page': projects.number,
        'has_next': projects.has_next(),
        'has_previous': projects.has_previous(),
        'next_page': projects.next_page_number() if projects.has_next() else None,
        'previous_page': projects.previous_page_number() if projects.has_previous() else None,
    }
    
    return render(request, 'all_project.html', context)

def filter_projects(request):
    # Get all filter parameters
    search_query = request.GET.get('search', '').strip()
    selected_techs = request.GET.getlist('techs')
    selected_categories = request.GET.getlist('categories')
    selected_years = request.GET.getlist('years')
    sort_by = request.GET.get('sort', 'newest')
    
    print(f"Search query: {search_query}")
    print(f"Selected technologies: {selected_techs}")
    print(f"Selected categories: {selected_categories}")
    print(f"Selected years: {selected_years}")
    print(f"Sorting by: {sort_by}")
    
    # Start with all projects
    projects = Project.objects.all()
    print(f"Total projects before filtering: {projects.count()}")
    
    # Apply search filter if provided
    if search_query:
        projects = projects.filter(
            models.Q(name__icontains=search_query) |
            models.Q(description__icontains=search_query) |
            models.Q(technology__name__icontains=search_query)
        ).distinct()
        print(f"Projects after search filtering: {projects.count()}")
    
    # Filter by technologies if selected
    if selected_techs:
        projects = projects.filter(technology__name__in=selected_techs).distinct()
        print(f"Projects after tech filtering: {projects.count()}")
    
    # Filter by categories if selected
    if selected_categories:
        projects = projects.filter(category__in=selected_categories)
        print(f"Projects after category filtering: {projects.count()}")
    
    # Filter by years if selected
    if selected_years:
        years = [int(year) for year in selected_years]
        projects = projects.filter(year__in=years)
        print(f"Projects after year filtering: {projects.count()}")
    
    # Sort projects based on the sort parameter
    if sort_by == 'newest':
        projects = projects.order_by('-created_at')
    elif sort_by == 'oldest':
        projects = projects.order_by('created_at')
    elif sort_by == 'name-asc':
        projects = projects.order_by('name')
    elif sort_by == 'name-desc':
        projects = projects.order_by('-name')
    
    print(f"Projects after sorting: {list(projects)}")
    
    context = {"projects": projects}
    print(f"Context being passed to template: {context}")
    
    return render(request, "partials/project_list.html", context)