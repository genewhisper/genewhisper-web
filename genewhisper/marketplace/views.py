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
from django.forms import ModelForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class ClinicalTrialView(CreateView, LoginRequiredMixin):
    login_url = reverse_lazy('login')
    model = ClinicalTrial
    success_url = reverse_lazy('marketplace:clinical_trial_list')
    fields = [

        'identifier', 'official_title', 'variants', 'genes',
        'start_date', 'end_date', 'number_of_participants',
        'offer_price', 'max_age', 'race', 'gender', 'clinical_trial_type',
        'min_age', 'brief_summary', 'detailed_description'
    ]


class ClinicalTrialListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = ClinicalTrial
    context_object_name = 'clinical_trial_list'


class ClinicalTrialUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('marketplace:clinical_trial_list')
    model = ClinicalTrial
    template_name = 'marketplace/create_clinical_trial.html'
    fields = [

        'identifier', 'official_title', 'variants', 'genes',
        'start_date', 'end_date', 'number_of_participants',
        'offer_price', 'max_age', 'race', 'gender', 'clinical_trial_type',
        'min_age', 'brief_summary', 'detailed_description'
    ]


class ClinicalTrialDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('marketplace:clinical_trial_list')
    model = ClinicalTrial
