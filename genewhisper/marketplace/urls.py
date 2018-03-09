from django.urls import path
from django.views.generic import TemplateView
from pathogenicity.views import ReportView

app_name = 'marketplace'

urlpatterns = [

    path('all-products', ReportView.as_view(template_name='marketplace/all_products.html'), name='all_products'),


]
