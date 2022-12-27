from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
  class Meta:
    model = Project # nazwa tabeli z ktorej zrobic formularz
    fields = '__all__' # ile pol wziac do formularza
