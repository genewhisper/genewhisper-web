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

    return render(request, 'projects/new_project_form.html', {'form': form, 'submitted': submitted})


class ProjectList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    # model = Project
    context_object_name = 'all_projects_list'

    def get_queryset(self):
        return Project.objects.filter(username=self.request.user)


class ProjectDetails(DetailView):
    model = Project
    template_name = 'projects/project_details.html'
    context_object_name = 'project_details'


class ProjectUpdate(UpdateView):
    model = Project
    template_name = 'projects/new_project_form.html'
    fields = ['name', 'company']


class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('projects:list_all_projects')
