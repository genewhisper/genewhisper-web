from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from marketplace.models import ClinicalTrial
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from pathogenicity.models import Pathogenicity, OncotatorOutput
from accounts.models import CompanyRegistration
from django.contrib.auth.models import User


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


class AllOffersView(TemplateView, LoginRequiredMixin):
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        all_genes = OncotatorOutput.objects.values_list('hugo_symbol', flat=True)
        # pathogenic_genes = Pathogenicity.objects.values_list('Pathogenicity', flat=True)
        queryset = ClinicalTrial.objects.all()

        for gene in all_genes:
            if Pathogenicity.objects.filter(Pathogenicity='Pathogenic'):
                context = queryset.filter(genes=gene)
                company_info = CompanyRegistration.objects.filter(pk=2)
                return {'context': context,
                        'company': company_info}
