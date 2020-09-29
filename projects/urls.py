from django.urls import path, include

from projects import views

app_name = 'projects'

urlpatterns = [
    path('all/', views.all_projects, name='all_projects'),
    path('home/', views.home, name='home'),
    path('<int:pk>', views.project_detail, name='project_detail'),

]
