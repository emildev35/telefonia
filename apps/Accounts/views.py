from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from .models import Usuario, CodigoProyecto


def home(request):
    return render(request, 'accounts/home.html', {})


def loginview(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=usuario, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('accounts_home'))
            else:
                return render(request, 'accounts/login.html', {'message': 'USUARIO NO ACTIVO'})
        else:
            return render(request, 'accounts/login.html', {'message': 'USUARIO O PASSWORD INCORECTO'})
    else:
        return render(request, 'accounts/login.html', {})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts_login'))


class UsuariosView(View):
    template_name = 'accounts/usuarios.html'
    ctx = {}

    @method_decorator(permission_required('accounts.add_usuario'))
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.filter(is_superuser=False).order_by('last_name')
        self.ctx['usuarios_list'] = usuarios
        return render(request, self.template_name, self.ctx)


class UsuarioDetail(View):
    template_name = 'accounts/detalle.html'
    ctx = {}

    @method_decorator(permission_required('accounts.add_usuario'))
    def get(self, request, *args, **kwargs):
        usuario = get_object_or_404(Usuario, id=int(kwargs['is_usuario']))
        self.ctx['usuario'] = usuario
        return render(request, self.template_name, self.ctx)

    @method_decorator(permission_required('accounts.add_usuario'))
    def post(self, request, *args, **kwargs):
        usuario = get_object_or_404(Usuario, id=int(kwargs['is_usuario']))
        CodigoProyecto.objects.create(
            id=int(request.POST['codigo']),
            usuario=usuario
        )
        self.ctx['usuario'] = usuario
        return render(request, self.template_name, self.ctx)
