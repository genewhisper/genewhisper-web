from django import forms
from django.forms import ModelForm
from .models import GenomicProfile


class NewGenomicProfileForm(ModelForm):
    class Meta:
        model = GenomicProfile

        fields = [

            'last_name', 'first_name', 'middle_init', 'physical_address', 'apt_number',
            'city', 'state', 'country', 'zip', 'phone', 'email', 'alternate_contact_name_and_number',
            'relationship', 'mailing_address', 'height_ft', 'height_inch', 'weight', 'dob', 'age', 'race',
            'gender', 'referral_name', 'referral_contact', 'priority', 'job_file', 'file_format', 'allow_sale'
        ]
        widgets = {

            'last_name': forms.TextInput(attrs={'class': 'form-control u-form-control rounded-0', }),
            'first_name': forms.TextInput(attrs={'class': 'form-control u-form-control rounded-0', }),
            'middle_init': forms.TextInput(attrs={'class': 'form-control u-form-control rounded-0', }),
            'physical_address': forms.TextInput(attrs={'class': 'form-control u-form-control rounded-0', }),
            'apt_number': forms.TextInput(attrs={'class': 'form-control u-form-control rounded-0', }),
            'city': forms.TextInput(attrs={'class': 'form-control u-form-control rounded-0', }),
            'state': forms.TextInput(attrs={'class': 'form-control u-form-control rounded-0', }),
            'country': forms.TextInput(attrs={'class': 'form-control u-form-control rounded-0', }),
            'zip': forms.TextInput(attrs={'class': 'form-control u-form-control rounded-0', }),
            'phone': forms.TextInput(attrs={'class': 'form-control u-form-control rounded-0', }),
            'email': forms.EmailInput(attrs={'class': 'form-control u-form-control rounded-0', }),
            'alternate_contact_name_and_number': forms.TextInput(
                attrs={'class': 'form-control u-form-control rounded-0', }),
            'relationship': forms.TextInput(attrs={'class': 'form-control u-form-control rounded-0', }),
            'mailing_address': forms.TextInput(attrs={'class': 'form-control u-form-control rounded-0', }),
            'height_ft': forms.TextInput(attrs={'class': 'form-control u-form-control rounded-0', }),
            'height_inch': forms.TextInput(attrs={'class': 'form-control u-form-control rounded-0', }),
            'weight': forms.TextInput(attrs={'class': 'form-control u-form-control rounded-0', }),
            'dob': forms.DateTimeInput(attrs={'class': 'form-control u-form-control rounded-0', }),
            'age': forms.TextInput(attrs={'class': 'form-control u-form-control rounded-0', }),
            'race': forms.Select(attrs={'class': 'form-control u-form-control rounded-0', }),
            'gender': forms.Select(attrs={'class': 'form-control u-form-control rounded-0', }),
            'referral_name': forms.TextInput(attrs={'class': 'form-control u-form-control rounded-0', }),
            'referral_contact': forms.TextInput(attrs={'class': 'form-control u-form-control rounded-0', }),
            'priority': forms.Select(attrs={'class': 'form-control u-form-control rounded-0', }),
            'job_file': forms.FileInput(attrs={'class': 'form-control u-form-control rounded-0', }),
            'file_format': forms.Select(attrs={'class': 'form-control u-form-control rounded-0', }),

        }
