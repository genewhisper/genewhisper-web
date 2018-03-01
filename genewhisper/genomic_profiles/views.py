from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .forms import NewGenomicProfileForm
from .models import GenomicProfile
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required(login_url=reverse_lazy('login'))
def create_new_genomic_profile(request):
    submitted = False
    if request.method == 'POST':
        form = NewGenomicProfileForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            try:
                project.username = request.user
            except Exception:
                pass
            project.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = NewGenomicProfileForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'profiles/new_genomic_profile.html', {'form': form, 'submitted': submitted})


class GenomicProfileListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = GenomicProfile
    context_object_name = 'all_genomic_profile_list'

    def get_queryset(self):
        return GenomicProfile.objects.filter(username=self.request.user)


class GenomicProfileDetailsView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = GenomicProfile
    context_object_name = 'genomic_profile_details'
    template_name = 'profiles/genomic_profile_details.html'


class GenomicProfileUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = GenomicProfile
    template_name = 'profiles/new_genomic_profile.html'
    fields = [

        'last_name', 'first_name', 'middle_init', 'physical_address', 'apt_number',
        'city', 'state', 'country', 'zip', 'phone', 'email', 'alternate_contact_name_and_number',
        'relationship', 'mailing_address', 'height_ft', 'height_inch', 'weight', 'dob', 'age', 'race',
        'gender', 'referral_name', 'referral_contact', 'priority', 'job_file', 'file_format', 'allow_sale'
    ]


class GenomicProfileDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = GenomicProfile
    success_url = reverse_lazy('profiles:all_genomic_profiles_list')
