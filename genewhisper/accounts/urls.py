from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [

    url(r'^login_company/$', views.login_company, name='login_company'),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('company-signup/', views.company_register, name='company_signup'),
    path('company-profile', views.CompanyProfileView.as_view(), name='company_profile')
]
