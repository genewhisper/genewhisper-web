from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from marketplace.models import ClinicalTrial
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from pathogenicity.models import Pathogenicity, OncotatorOutput
from accounts.models import CompanyRegistration
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from marketplace.forms import ClinicalTrialForm
from django.http import HttpResponseRedirect
from django.shortcuts import render


@login_required(login_url=reverse_lazy('login'))
def create_new_clinical_trial(request):
    submitted = False
    if request.method == 'POST':
        form = ClinicalTrialForm(request.POST, request.FILES)
        if form.is_valid():
            clinical_trial = form.save(commit=False)
            try:
                clinical_trial.username = request.user
            except Exception:
                pass
            clinical_trial.save()
            return HttpResponseRedirect('clinical-trial-list')
    else:
        form = ClinicalTrialForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'marketplace/create_clinical_trial.html', {'form': form, 'submitted': submitted})


class ClinicalTrialListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = ClinicalTrial
    context_object_name = 'clinical_trial_list'

    def get_queryset(self):
        return ClinicalTrial.objects.filter(username=self.request.user)


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
                company_info = CompanyRegistration.objects.filter()[0].companyName
                return {'context': context,
                        'company': company_info}


class FileManagerView(TemplateView, LoginRequiredMixin):
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return ClinicalTrial.objects.filter(username=self.request.user)


class ShoppingCartView(TemplateView, LoginRequiredMixin):
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return ClinicalTrial.objects.filter(username=self.request.user)
