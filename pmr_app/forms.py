from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.widgets.TextInput(attrs={ 'class': 'form-control' })
    )
    password = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.widgets.PasswordInput(attrs={ 'class': 'form-control' })
    )

    def clean(self):
        user = User.objects.filter(username = self.cleaned_data['username'])
        if not user.exists():
            self.add_error('username', 'Username does not exist.')

class UserSignUpForm(UserLoginForm):

    def clean(self):
        user = User.objects.filter(username = self.cleaned_data['username'])
        if user.exists():
            self.add_error('username', 'Username already exists.')
