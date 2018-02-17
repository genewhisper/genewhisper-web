from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .forms import NewProjectForm
from .models import Project
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required(login_url=reverse_lazy('login'))
def create_new_project(request):
    submitted = False
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            try:
                project.username = request.user
            except Exception:
                pass
            project.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = NewProjectForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'profiles/new_project.html', {'form': form, 'submitted': submitted})


class ProjectListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Project
    context_object_name = 'all_projects_list'

    def get_queryset(self):
        return Project.objects.filter(username=self.request.user)


class ProjectDetailsView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = Project
    context_object_name = 'project_details'
    template_name = 'profiles/project_details.html'


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Project
    template_name = 'profiles/new_project.html'
    fields = [
        'name', 'position', 'company', 'address',
        'phone', 'email', 'description',
        'project_status', 'priority', 'file_format', 'job_file',
    ]


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Project
    success_url = reverse_lazy('profiles:all_projects_list')
