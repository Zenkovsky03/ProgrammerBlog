from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
  class Meta:
    model = Project # nazwa tabeli z ktorej zrobic formularz
    fields = ['title', 'description', 'demo_link', 'source_link', 'tags'] # ile pol wziac do formularza '__all__'
