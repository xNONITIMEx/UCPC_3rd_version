
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView
from .models import Cards


class Index(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        contex = {}
        if request.user.is_authenticated:
            cards = Cards.objects.filter()
            contex['cards'] = cards
        return render(request, self.template_name, contex)


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






