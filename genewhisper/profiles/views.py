from django.views.generic import TemplateView
from projects.models import Project

class ProfilePage(TemplateView):
    template_name = 'profiles/profile.html'

