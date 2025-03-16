from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:id>', views.single_project, name='single-project'),
]