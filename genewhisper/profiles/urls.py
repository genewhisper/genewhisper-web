from django.urls import path
from projects.views import ProjectList
from profiles import views

app_name = 'profiles'

urlpatterns = [
    path('', views.ProfilePage.as_view(), name='profile'),

    path('', ProjectList.as_view(), name='all_project_list'),

]
