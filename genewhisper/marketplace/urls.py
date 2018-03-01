from django.urls import path
from django.views.generic import TemplateView
from marketplace.views import all_products_list
app_name = 'marketplace'

urlpatterns = [

    # path('all-products', TemplateView.as_view(template_name='marketplace/all_products.html'), name='all_products'),

    path('all-products', all_products_list, name='all_products'),

]
