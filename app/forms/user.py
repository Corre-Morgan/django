from django.forms import models

from app.models import User


class UserForm(models.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']