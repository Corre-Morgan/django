from django.forms import Form, widgets
from django import forms


class RegisterForm(Form):
    username = forms.CharField(max_length=200, min_length=4)
    email = forms.CharField(max_length=200, min_length=4,
                            widget=widgets.EmailInput(attrs={'placeholder': 'Email'}))
    password_1 = forms.CharField(max_length=200, min_length=4,
                                 widget=widgets.PasswordInput(attrs={'placeholder': 'Password'}))
    password_2 = forms.CharField(max_length=200, min_length=4,
                                 widget=widgets.PasswordInput(attrs={'placeholder': 'Repeat password'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.isalnum():
            self.add_error('username', 'Only alphanum chars allowed')
            return None
        return username

    def clean(self):
        password_1 = self.cleaned_data['password_1']
        password_2 = self.cleaned_data['password_2']
        if password_1 != password_2:
            self.add_error('password_1', 'enter the same password')
        return super().clean()

