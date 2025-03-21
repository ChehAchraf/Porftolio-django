from django.contrib import admin
from .models import (
    PersonalInfo, TechnichalExpertise, Technology, Project, 
    ProjectTechnology, ProjectDetail, ProjectMetric, 
    DevelopmentStage, Challenges, ProjectGallery
)

# Register your models here.
admin.site.register(PersonalInfo)
admin.site.register(TechnichalExpertise)
admin.site.register(Technology)
admin.site.register(Project)
admin.site.register(ProjectTechnology)

class ProjectMetricInline(admin.TabularInline):
    model = ProjectMetric
    extra = 1

class DevelopmentStageInline(admin.TabularInline):  
    model = DevelopmentStage
    extra = 1  

class ChallengesInline(admin.TabularInline):  
    model = Challenges
    extra = 1  

@admin.register(ProjectDetail)
class ProjectDetailAdmin(admin.ModelAdmin):
    list_display = ('project', 'project_overview')
    inlines = [ProjectMetricInline, DevelopmentStageInline, ChallengesInline]
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('project')

@admin.register(DevelopmentStage)
class DevelopmentStageAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'week')
    ordering = ('project', 'week')  

@admin.register(Challenges)
class ChallengesAdmin(admin.ModelAdmin):
    list_display = ('project', 'title')
    ordering = ('project',)  

@admin.register(ProjectGallery)
class ProjectGalleryAdmin(admin.ModelAdmin):
    list_display = ('project', 'title', 'order', 'created_at')
    list_filter = ('project', 'created_at')
    search_fields = ('title', 'description', 'project__name')
    ordering = ('project', 'order', 'created_at')
    list_per_page = 20

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('project')
