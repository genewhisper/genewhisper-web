from django import forms
from django.forms import ModelForm
from .models import Project


class NewProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'name', 'position', 'company', 'address',
            'phone', 'email', 'web', 'description',
            'project_status', 'priority', 'job_file', 'file_format'
        ]
