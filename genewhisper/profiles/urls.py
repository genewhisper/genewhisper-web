from django.urls import path
from profiles import views
from genomic_profiles import views as genomic_profile_views
from pathogenicity import views as pathogenicity_views
from marketplace import views as marketplace_views

app_name = 'profiles'

urlpatterns = [

    path('', genomic_profile_views.GenomicProfileListView.as_view(template_name='profiles/profile.html'),
         name='main_profile_page'),

    path('my-genomic-profiles',
         genomic_profile_views.GenomicProfileListView.as_view(template_name='profiles/genomic_profiles.html'),
         name='my_genomic_profiles'),

    path('new-genomic-profile', genomic_profile_views.create_new_genomic_profile, name='new_genomic_profile_form'),

    path('genomic-profile-list',
         genomic_profile_views.GenomicProfileListView.as_view(template_name='profiles/genomic_profile_list.html'),
         name='all_genomic_profiles_list'),

    path('genomic-profile-details/<int:pk>', genomic_profile_views.GenomicProfileDetailsView.as_view(),
         name='genomic_profile_details'),

    path('genomic-profile-update/<int:pk>', genomic_profile_views.GenomicProfileUpdateView.as_view(),
         name='genomic_profile_update'),

    path('genomic-profile-delete/<int:pk>', genomic_profile_views.GenomicProfileDeleteView.as_view(),
         name='genomic_profile_delete'),

    path('genomic-profile-report/<int:pk>',
         pathogenicity_views.ReportView.as_view(template_name='profiles/genomic_profile_report.html'), name='report'),

    path('my-genomic-reports',
         pathogenicity_views.ReportView.as_view(template_name='profiles/genomic_reports.html'),
         name='my_genomic_reports'),

    path('genomic-report-list',
         genomic_profile_views.GenomicProfileListView.as_view(template_name='profiles/genomic_report_list.html'),
         name='all_genomic_report_list'),
]
