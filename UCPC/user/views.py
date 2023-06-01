from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView
from django.contrib import messages

from .forms import UserRegisterForm


class Login(FormView):
    form_class = AuthenticationForm
    success_url = '/'
    template_name = 'login.html'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(Login, self).form_valid(form)

    def from_invalid(self, form):
        return super(Login, self).form_invalid(form)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} создан!')
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

