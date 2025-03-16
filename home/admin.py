from django.contrib import admin
from .models import PersonalInfo, TechnichalExpertise, Technology, Project, ProjectTechnology, ProjectDetail, Criteria,DevelopmentStage , Challenges

# Register your models here.
admin.site.register(PersonalInfo)
admin.site.register(TechnichalExpertise)
admin.site.register(Technology)
admin.site.register(Project)
admin.site.register(ProjectTechnology)
admin.site.register(Criteria)

class DevelopmentStageInline(admin.TabularInline):  
    model = DevelopmentStage
    extra = 1  

class ChallengesInline(admin.TabularInline):  
    model = Challenges
    extra = 1  

@admin.register(ProjectDetail)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project', 'detail')
    inlines = [DevelopmentStageInline, ChallengesInline] 

@admin.register(DevelopmentStage)
class DevelopmentStageAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'week')
    ordering = ('project', 'week')  

@admin.register(Challenges)
class ChallengesAdmin(admin.ModelAdmin):
    list_display = ('project', 'title')
    ordering = ('project',)  
