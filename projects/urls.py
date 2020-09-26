from django.urls import path, include

from projects import views

urlpatterns = [
    path('', views.all_projects),
]
