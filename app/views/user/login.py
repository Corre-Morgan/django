from django.conf import settings
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'registration/login.html'

    def login(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect('home.html')
        else:
            return render(request, self.template_name)
