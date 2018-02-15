from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from projects.models import Project


class ProfilePage(ListView,LoginRequiredMixin ):
    login_url = reverse_lazy('login')
    model = Project
    context_object_name = 'all_projects_list'
