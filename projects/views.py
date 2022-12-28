from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
# Create your views here.

def projects(request):
  projects = Project.objects.all()
  context = {
    'projects' : projects,
  }
  return render(request, 'projects/projects.html', context)

def project(request, pk):
  projectObj = Project.objects.get(id=pk)
  context = {
    'project' : projectObj,
  }
  return render(request, 'projects/single-project.html', context)


def createProject(request):
  form = ProjectForm()

  if request.method == 'POST': # jesli wyslalismy POSTA to :
    form = ProjectForm(request.POST, request.FILES) # przetworzenie formularza
    if form.is_valid():
      form.save() # zapisanie obiektu i mozemy dodac do bazy danych
      return redirect('projects') # po name w views

  context = {
    'form' : form,
  }
  return render(request, 'projects/project_form.html', context)

def updateProject(request, pk):
  project = Project.objects.get(id = pk) # pobranie odpowiedniego projektu
  form = ProjectForm(instance=project) # zapisanie go do formularza

  if request.method == 'POST': # jesli wyslalismy POSTA to :
    form = ProjectForm(request.POST, request.FILES ,instance=project) # przetworzenie formularza
    if form.is_valid():
      form.save() # zapisanie obiektu i mozemy dodac do bazy danych
      return redirect('projects') # po name w views

  context = {
    'form' : form,
  }
  return render(request, 'projects/project_form.html', context)

def deleteProject(request, pk):
  project = Project.objects.get(id=pk)
  if request.method == 'POST': # jesli wyslalismy POSTA to :
    project.delete() # usuwamy obiekt
    return redirect('projects') # zmiana linku na katalog glowny
  context = {
    'object' : project,
  }
  return render(request, 'projects/delete_template.html', context)