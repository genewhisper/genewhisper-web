from django.urls import path
from django.views.generic import TemplateView
from pathogenicity.views import ReportView
from marketplace import views

app_name = 'marketplace'

urlpatterns = [

    path('all-products', ReportView.as_view(template_name='marketplace/all_products.html'), name='all_products'),

    # path('new-clinical-trial', views.ClinicalTrialView.as_view(template_name='marketplace/create_clinical_trial.html'),
    #      name='new_clinical_trial'),

    path('new-clinical-trial', views.create_new_clinical_trial, name='new_clinical_trial'),

    path('clinical-trial-list',
         views.ClinicalTrialListView.as_view(template_name='marketplace/clinical_trial_list.html'),
         name='clinical_trial_list'),

    path('all-clinical-trails',
         views.AllClinicalTrialsView.as_view(template_name='marketplace/all_clinical_trials.html'),
         name='all_clinical_trials'),


    path('clinical-trial/update/<int:pk>', views.ClinicalTrialUpdateView.as_view(), name='clinical_trial_update'),

    path('clinical-trial/delete/<int:pk>', views.ClinicalTrialDeleteView.as_view(), name='clinical_trial_delete'),

    path('all-offers-list', views.AllOffersView.as_view(template_name='marketplace/all_offers_list.html'), name='all_offers_list'),

    path('all-offers', views.AllOffersView.as_view(template_name='marketplace/all_offers.html'), name='all_offers'),




    path('file-manager', views.FileManagerView.as_view(template_name='marketplace/file_manager.html'),
         name='file_manager'),

    path('shopping-cart', views.ShoppingCartView.as_view(template_name='marketplace/shopping_cart.html'),
         name='shopping_cart')
]
