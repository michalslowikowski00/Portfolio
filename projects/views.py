from django.shortcuts import render
from projects.models import Project

# Create your views here.


def all_projects(request):
    """Query the db to return all project objects"""

    projects = Project.objects.all()
    return render(request, "projects/all_projects.html", {"projects": projects})


def project_detail(request, pk):
    """
    :param request: HttpRequest object
    :type request: Any
    :param pk: primary key from DB
    :type pk: int
    """
    project = Project.objects.get(pk=pk)
    return render(request, "projects/detail.html", {"project": project})
