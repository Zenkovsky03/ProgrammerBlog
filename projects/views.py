from django.shortcuts import render
from django.http import HttpResponse
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
  page = "projects"
  number = 10
  context = {
    'page' : page,
    'number' : number,
    'projects' : projectList
  }
  return render(request, 'projects/projects.html', context)

def project(request, pk):
  projectObj = None
  for i in projectList:
    if i['id'] == pk:
      projectObj = i
  return render(request, 'projects/single-project.html', {'project' : projectObj})
