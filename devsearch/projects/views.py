from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def projects(request):
    projectsObj = Project.objects.all()
    context = {'projects' : projectsObj}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project' : projectObj})

