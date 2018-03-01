from django.shortcuts import render
from marketplace.forms import AddProductForm
from django.http import HttpResponseRedirect
from genomic_profiles.forms import NewGenomicProfileForm
from genomic_profiles.models import GenomicProfile
from genomic_profiles.models import GenomicProfile
from genomic_profiles.models import GenomicProfile
from django.views.generic import TemplateView
from django.urls import reverse_lazy


# Create your views here.

def all_products_list(request):
    product = GenomicProfile.objects.all()
    return render(request, 'marketplace/all_products.html', {'product': product})

