from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from apps.utils.db import procedure
from apps.Llamadas.models import Llamada


def home(request):
    if request.user == AnonymousUser():
        return HttpResponseRedirect(reverse('seguridad_login'))
    else:
        return HttpResponseRedirect(reverse('home_home'))


class HomeView(TemplateView):
    template_name = 'home/home.html'

    @method_decorator(permission_required('llamadas.add_llamada'))
    def get(self, request, *args, **kwargs):
        llamadas = procedure('timecall_usuario', 2, 1)
        c_llamadas = Llamada.objects.count()
        c_llamadas_entrantes = Llamada.objects.filter(tipo_llamada=1).count()
        c_llamadas_salientes = Llamada.objects.filter(tipo_llamada=2).count()
        c_llamadas_operador = Llamada.objects.filter(tipo_llamada=3).count()
        ctx = {
            'llamadas': llamadas,
            'total_llamadas': c_llamadas,
            'total_llamadas_entrantes': c_llamadas_entrantes,
            'total_llamadas_salientes': c_llamadas_salientes,
            'total_llamadas_operador': c_llamadas_operador
        }
        return render(request, self.template_name, ctx)


def handler404(request):
    return render(request, '404.html', {})
