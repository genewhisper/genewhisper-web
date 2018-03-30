from django.shortcuts import render
from pathogenicity.models import Pathogenicity
from genomic_profiles.models import GenomicProfile
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class ReportView(TemplateView, LoginRequiredMixin):

    def get_context_data(self, *args, **kwargs, ):
        genomic_profile_id = GenomicProfile(self, *args, **kwargs)
        genomic_profile_data = GenomicProfile.objects.all().filter(username=self.request.user)

        all_variants_number = Pathogenicity.objects.all().count()

        benign_variants_number = Pathogenicity.objects.filter(Pathogenicity='Benign').count()
        benign_variants_procent = (benign_variants_number * 100 / all_variants_number).__format__('7.2f')

        likely_benign_variants_number = Pathogenicity.objects.filter(Pathogenicity='Likely_benign').count()
        likely_benign_variants_procent = (likely_benign_variants_number * 100 / all_variants_number).__format__('7.2f')

        uncertain_significance_variants_number = Pathogenicity.objects.filter(
            Pathogenicity='Uncertain_significance').count()
        uncertain_significance_variants_procent = (
                uncertain_significance_variants_number * 100 / all_variants_number).__format__('7.2f')

        likely_pathogenic_variants_number = Pathogenicity.objects.filter(Pathogenicity='Likely_pathogenic').count()
        likely_pathogenic_variants_procent = (likely_pathogenic_variants_number * 100 / all_variants_number).__format__(
            '7.2f')

        pathogenic_variants_number = Pathogenicity.objects.filter(Pathogenicity='Pathogenic').count()
        pathogenic_variants_procent = (pathogenic_variants_number * 100 / all_variants_number).__format__(
            '7.2f')

        context = {
            'genomic_profile_id': genomic_profile_id,
            'genomic_profile_data': genomic_profile_data,

            'all_variants_number': all_variants_number,

            'benign_variants_number': benign_variants_number,
            'benign_variants_procent': benign_variants_procent,

            'likely_benign_variants_number': likely_benign_variants_number,
            'likely_benign_variants_procent': likely_benign_variants_procent,

            'uncertain_significanse_variants_number': uncertain_significance_variants_number,
            'uncertain_significance_variants_procent': uncertain_significance_variants_procent,

            'likely_pathogenic_variants_number': likely_pathogenic_variants_number,
            'likely_pathogenic_variants_procent': likely_pathogenic_variants_procent,

            'pathogenic_variants_number': pathogenic_variants_number,
            'pathogenic_variants_procent': pathogenic_variants_procent
        }

        return context
