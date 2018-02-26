from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class ReportTemplateView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    context_object_name = 'report'
