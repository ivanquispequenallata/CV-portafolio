#los codigos de aqui se veran en  el portafolio
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import InformationsCV


class index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perfil'] = InformationsCV.objects.first()
        return context


