from django.shortcuts import render
from django.http import HttpResponseRedirect
from genomic_profiles.forms import NewGenomicProfileForm
from genomic_profiles.models import GenomicProfile
from genomic_profiles.models import GenomicProfile
from genomic_profiles.models import GenomicProfile
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from marketplace.models import ClinicalTrial
from django.views.generic import CreateView
from marketplace.forms import ClinicalTrialForm


# Create your views here.
class ClinicalTrialView(CreateView):
    model = ClinicalTrial
    form_class = ClinicalTrialForm
    fields = [

        'identifier', 'official_title', 'variants', 'genes',
        'start_date', 'end_date', 'number_of_participants',
        'offer_price', 'max_age', 'race', 'gender', 'clinical_trial_type',
        'min_age', 'brief_summary', 'detailed_description'
    ]