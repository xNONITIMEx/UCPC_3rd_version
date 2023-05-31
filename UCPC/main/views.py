from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, FormView, CreateView, UpdateView
from django.contrib import messages

from .models import Cards


class Index(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        contex = {}
        if request.user.is_authenticated:
            cards = Cards.objects.filter()
            contex['cards'] = cards
        return render(request, self.template_name, contex)


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


class AddCard(CreateView):
    fields = ['title', 'desc', 'tags']
    model = Cards
    success_url = '/'
    template_name = 'add_edit_card.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        for tag in form.cleaned_data['tags']:
            self.object.tags.add(tag.id)
        self.object.save()
        return redirect(self.success_url)


class EditCard(UpdateView):
    model = Cards
    fields = ['title', 'desc', 'tags']
    success_url = '/'
    template_name = 'add_edit_card.html'

    def get_object(self, queryset=None):
        obj = Cards.objects.get(id=self.kwargs['pk'])
        return obj


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} создан!')
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



