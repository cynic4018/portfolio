from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #Call super to get the context data
        context['about'] = About.objects.first()
        context['skills'] = Skills.objects.all()
        context['works'] = RecentWork.objects.all()

        return context