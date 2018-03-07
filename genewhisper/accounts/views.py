from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
# Create your views here.
from django.shortcuts import redirect

from accounts.forms import UserCreateForm, CompanyCreateForm


class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/singup.html'


def company_register(request):
    registered = False
    success_url = reverse_lazy('login')
    if request.method == 'POST':
        user_form = UserCreateForm(data=request.POST)
        company_form = CompanyCreateForm(data=request.POST)

        if user_form.is_valid() and company_form.is_valid():
            user = user_form.save()
            company = company_form.save(commit=False)
            user.set_password(user.password)  # hashing the password
            user.save()

            company.user = user  # seting up one to one relationship with user
            company.save()

            registered = True

            return redirect('login')

        else:
            print(user_form.errors, company_form.errors)
    else:
        user_form = UserCreateForm()
        company_form = CompanyCreateForm()

    return render(request, 'accounts/company_singup.html',
                  {'user_form': user_form,
                   'company_form': company_form,
                   'registered': registered}
                  )
