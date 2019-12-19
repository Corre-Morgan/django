from django.contrib.auth.models import User
from django.views.generic import FormView

from app.forms.register import RegisterForm
from app.models import Person


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password_1 = form.cleaned_data['password_1']
        user = User.objects.create_user(username=username, email=email, password=password_1)
        person = Person.objects.create(user=user)
        person.save()
        return super().form_valid(form)