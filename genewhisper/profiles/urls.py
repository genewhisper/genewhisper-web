from django.urls import path
from projects.views import ProjectList
from profiles import views

app_name = 'profiles'

urlpatterns = [
    path('', views.ProfilePage.as_view(), name='main_profile_page'),


]
