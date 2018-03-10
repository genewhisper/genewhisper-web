from django.urls import path
from django.views.generic import TemplateView
from pathogenicity.views import ReportView
from marketplace.views import ClinicalTrialView

app_name = 'marketplace'

urlpatterns = [

    path('all-products', ReportView.as_view(template_name='marketplace/all_products.html'), name='all_products'),

    path('new-clinical-trial', ClinicalTrialView.as_view(template_name='marketplace/create_clinical_trial.html'),
         name='new_clinical_trial')

]
