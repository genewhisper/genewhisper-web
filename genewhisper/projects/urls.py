from django.urls import path
from projects import views

app_name = 'projects'

urlpatterns = [
    path('new-project/', views.create_new_project, name='new_project_form'),

    path('projects-list/', views.ProjectList.as_view(template_name='projects/project_list.html'),
         name='list_all_projects'),
    path('<int:pk>', views.ProjectDetails.as_view(), name='project_details'),
    path('update/<int:pk>', views.ProjectUpdate.as_view(), name='project_update'),
    path('delete/<int:pk>', views.ProjectDelete.as_view(), name='project_delete'),
]
