from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Cards


def index(request):
    return render(request, 'index.html')

class Index(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        contex = {}
        if request.user.is_authenticated:
            news = Cards.objects.filter(author=request.user)
            contex['news'] = news
        return render(request, self.template_name, contex)



