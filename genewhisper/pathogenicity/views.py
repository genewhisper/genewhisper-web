from django.shortcuts import render
from pathogenicity.models import Pathogenicity
from genomic_profiles.models import GenomicProfile
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


@login_required(login_url=reverse_lazy('login'))
def report_info(request, genomicprofile_id):

    genomic_profile_id = GenomicProfile.objects.get(pk=genomicprofile_id)

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

    return render(
        request, 'profiles/genomic_profile_report.html',

        {
            'genomic_profile_id': genomic_profile_id,

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
    )
