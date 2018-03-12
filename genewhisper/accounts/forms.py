from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CompanyRegistration
from .models import UserInfo


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        model = UserInfo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['email'].label = 'Email address'


class CompanyRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ('companyName', 'address', 'companyUrl', 'companyEmail', 'companyPhone')
        model = CompanyRegistration
