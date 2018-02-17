from django.urls import path
from profiles import views
from projects import views as project_views

app_name = 'profiles'

urlpatterns = [

    path('', project_views.ProjectListView.as_view(template_name='profiles/profile.html'), name='main_profile_page'),
    path('new-project', project_views.create_new_project, name='new_project_form'),
    path('project-list', project_views.ProjectListView.as_view(template_name='profiles/project_list.html'),
         name='all_projects_list'),
    path('project-details/<int:pk>', project_views.ProjectDetailsView.as_view(), name='project_details'),
    path('project-update/<int:pk>', project_views.ProjectUpdateView.as_view(), name='project_update'),


    path('project-delete/<int:pk>', project_views.ProjectDeleteView.as_view(), name='project_delete'),
]
