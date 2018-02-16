from django import forms
from django.forms import ModelForm
from .models import Project


class NewProjectForm(ModelForm):
    class Meta:
        model = Project

        fields = [
            'name', 'position', 'company', 'address',
            'phone', 'email',  'description',
            'project_status', 'priority', 'file_format', 'job_file',
        ]
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control u-form-control rounded-0', }),
        #     'position': forms.TextInput(attrs={'class': 'form-control form-control-md rounded-0'}),
        #     'company': forms.TextInput(attrs={'class': 'form-control form-control-md rounded-0'}),
        #     'address': forms.TextInput(attrs={'class': 'form-control form-control-md rounded-0'}),
        #     'phone': forms.TextInput(attrs={'class': 'form-control form-control-md rounded-0'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control form-control-md rounded-0'}),
        #     'web': forms.URLInput(attrs={'class': 'form-control form-control-md rounded-0'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control form-control-md rounded-0'}),
        #     'project_status': forms.Select(attrs={'class': 'form-control rounded-0'}),
        #     'priority': forms.Select(attrs={'class': 'form-control rounded-0'}),
        #     'file_format': forms.Select(attrs={'class': 'form-control rounded-0'}),
        #     'job_file': forms.FileInput(attrs={'class': 'js-file-attachment'}),
        #
        # }
