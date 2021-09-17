from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    ordered_field_names = ['username', 'first_name', 'last_name']
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2','first_name', 'last_name')
        field_order = ['username', 'password1', 'password2', 'first_name', 'last_name']
