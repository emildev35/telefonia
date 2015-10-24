from django_ajax.decorators import ajax
from drealtime import iShoutClient
from django.views.generic import View
from django.shortcuts import render
from apps.Accounts.models import Usuario
from .models import Alerta


class ShowAllView(View):
    template_name = 'notificaciones/all.html'

    def get(self, request):
        notificaciones = Alerta.objects.filter(usuario=request.user).filter(visto=False)
        notificaciones.update(visto=True)
        return render(request, self.template_name, {'notificaciones': notificaciones})


@ajax
def visto(request):
    Alerta.objects.filter(usuario=request.user).update(visto=True)
    return {}


def usuarioNotificaciones(id_usuario):
    ishoutclient = iShoutClient()
    ishoutclient.emit(
        id_usuario,
        'notificaciones',
        data={'msg': 'Tu saldo disponible es Bs 00.00', 'type': 'danger'}
    )


def adminNotificaciones():
    administradores = Usuario.objects.filter(is_staff=True)
    ishoutclient = iShoutClient()
    for admin in administradores:
        ishoutclient.emit(
            admin.id,
            'notificaciones',
            data={
                'msg': 'Al usuario pepe le queda de saldo Bs 00.00',
                'type': 'danger'
            }
        )
