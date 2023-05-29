from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, FormView

from .models import Cards


def index(request):
    return render(request, 'index.html')

class Index(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        contex = {}
        if request.user.is_authenticated:
            cards = Cards.objects.filter(author=request.user)
            contex['cards'] = cards
        return render(request, self.template_name, contex)


class Login(FormView):
    form_class = AuthenticationForm
    success_url = 'home'
    template_name = 'login.html'

    def form_valid(self, form):
        self.user = form.ger_user()
        login(self.request, self.user)
        return super(LoginView, self).form_valid()

    def from_invalid(self):
        return super(LoginView, self).form_invalid()


class Logout(View):
    def get(self, request):
        logout(request)
        redirect('home')
