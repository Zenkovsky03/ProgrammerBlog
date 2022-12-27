from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.

projectList = [
  {
    'id' : '1',
    'tittle' : 'Ecommerce Website',
    'description' : 'Fully ecommercial website'
  },
  {
    'id' : '2',
    'tittle' : 'Portfolio website',
    'description' : 'This is project where i build out my portfolio'
  },
  {
    'id' : '3',
    'tittle' : 'Social network',
    'description' : 'Open source project avaiable now!'
  }
]

def projects(request):
  projects = Project.objects.all()
  context = {
    'projects' : projects,
  }
  return render(request, 'projects/projects.html', context)

def project(request, pk):
  projectObj = Project.objects.get(id=pk)
  return render(request, 'projects/single-project.html', {'project' : projectObj,})
