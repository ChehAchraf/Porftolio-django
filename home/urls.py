from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:id>', views.single_project, name='single-project'),
    path('project/all', views.all_project , name="all_project"),
    path('filter/', views.filter_projects, name="filter_projects"),
]