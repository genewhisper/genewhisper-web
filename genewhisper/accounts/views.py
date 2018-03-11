from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.models import User
# Create your views here.
from django.shortcuts import redirect


from .forms import UserCreateForm, CompanyRegistrationForm,CompanyRegistration


class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/singup.html'


def login_company(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'accounts/company_dashboard.html', {"message": "success"})
            else:
                return render(request, 'accounts/company_login.html',
                              {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'accounts/company_login.html',
                          {"error_message": "Username and password are not valid!"})
    return render(request, 'accounts/company_login.html', {"error_message": ""})


def company_register(request):
    form = CompanyRegistrationForm(request.POST or None)

    if form.is_valid():
        u = User.objects.create_user(
            request.POST['username'], request.POST['companyEmail'], request.POST['password'], is_active=1)
        companyRegistration = CompanyRegistration()
        companyRegistration.companyName = request.POST['companyName']
        companyRegistration.address = request.POST['address']
        companyRegistration.companyUrl = request.POST['companyUrl']
        companyRegistration.companyEmail = request.POST['companyEmail']
        companyRegistration.companyPhone = request.POST['companyPhone']
        companyRegistration.user = u
        companyRegistration.save()
        form = CompanyRegistrationForm()
        return render(request, 'accounts/company_login.html', {"error_message": ""})


    context = {"form": form, }
    return render(request, 'accounts/singup.html', context)


class CompanyProfileView(TemplateView):
    template_name = 'accounts/company_dashboard.html'