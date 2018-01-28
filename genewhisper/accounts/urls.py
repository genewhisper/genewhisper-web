from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    url('login/',
        auth_views.LoginView.as_view(temmpale_name='accounts.login.html'),
        name='login'),
    url('logout/', auth_views.LogoutView(), name='logout'),
    url('signup', views.SingUp.as_view(), name='signup')
]
