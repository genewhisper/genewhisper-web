from django.shortcuts import render
from pathogenicity.models import Pathogenicity


def pathogenicity_request(request):
    data = Pathogenicity.objects.all()
    return render(request, 'profiles/genomic_profile_report.html', {'data': data})
