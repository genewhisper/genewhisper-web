from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Company
from accounts.models import UserInfo


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        model = UserInfo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'Email address'


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        fields = ('company_name', 'company_url', 'company_phone_number')
        model = Company


