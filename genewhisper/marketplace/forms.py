from django import forms
from django.forms import ModelForm
from django.forms.widgets import Select
from genomic_profiles.models import GenomicProfile


class AddProductForm(forms.Form):
    product = forms.ModelChoiceField(queryset=GenomicProfile.objects.values('id', 'first_name', 'last_name'))
# class Meta:
#     CHOICES = GenomicProfile.objects.all()
#
#     model = GenomicProfile
#     fields = ('first_name',)
#     widgets = {
#         'first_name': Select(choices=((x.id, x.first_name) for x in CHOICES)),
#     }
