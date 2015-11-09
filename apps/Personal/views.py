from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.shortcuts import get_object_or_404
from apps.Accounts.models import CodigoUsuario, Extension
from django.views.generic.edit import CreateView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from django.core.urlresolvers import reverse_lazy
from .models import Cargo, Area, Funcionario
from .serializers import CargoSerializer, AreaSerializer, FuncionarioSerializer


class CargoView(CreateView):
    model = Cargo
    template_name = 'cargo/create.html'
    fields = ['descripcion']
    success_url = reverse_lazy('personal_cargo_create')


class CargoMixin(object):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class CargoList(CargoMixin, ListAPIView):
    """ Clase que retorna un listado de los CargoList"""
    pass


class CargoDetail(CargoMixin, RetrieveUpdateDestroyAPIView):
    """ Gestor del api"""
    pass


class AreaView(CreateView):
    model = Area
    template_name = 'area/create.html'
    fields = ['descripcion']
    success_url = reverse_lazy('personal_area_create')


class AreaMixin(object):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class AreaList(AreaMixin, ListAPIView):
    """ Clase que retorna un listado de los CargoList"""
    pass


class AreaDetail(AreaMixin, RetrieveUpdateDestroyAPIView):
    """ Gestor del api"""
    pass


class FuncionarioView(CreateView):
    model = Funcionario
    template_name = 'funcionario/create.html'
    success_url = reverse_lazy('personal_funcionario_create')
    fields = ('id', 'first_name', 'last_name', 'username', 'fecha_nacimiento', 'ci', 'ip', 'cargo', 'area', 'fotografia')


class FuncionarioMixin(object):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer


class FuncionarioList(FuncionarioMixin, ListAPIView):
    """ Clase que retorna un listado de los CargoList"""
    pass


class FuncionarioDetail(FuncionarioMixin, RetrieveUpdateDestroyAPIView):
    """ Gestor del api"""
    pass


class FuncionariosView(View):
    template_name = 'accounts/usuarios.html'
    ctx = {}

    @method_decorator(permission_required('accounts.add_funcionario'))
    def get(self, request, *args, **kwargs):
        funcionario = Funcionario.objects.filter(is_superuser=False).order_by('last_name')
        self.ctx['usuarios_list'] = funcionario
        return render(request, self.template_name, self.ctx)


class UsuarioDetail(View):
    template_name = 'accounts/detalle.html'
    ctx = {}

    @method_decorator(permission_required('accounts.add_usuario'))
    def get(self, request, *args, **kwargs):
        usuario = get_object_or_404(Funcionario, id=int(kwargs['is_usuario']))
        self.ctx['usuario'] = usuario
        return render(request, self.template_name, self.ctx)

    @method_decorator(permission_required('accounts.add_usuario'))
    def post(self, request, *args, **kwargs):
        usuario = get_object_or_404(Funcionario, id=int(kwargs['is_usuario']))
        CodigoUsuario.objects.create(
            id=int(request.POST['codigo']),
            usuario=usuario
        )
        self.ctx['usuario'] = usuario
        return render(request, self.template_name, self.ctx)


class FuncionariosLista(View):
    template_name = 'funcionario/usuarios.html'
    ctx = {}

    @method_decorator(permission_required('accounts.add_funcionario'))
    def get(self, request, *args, **kwargs):
        funcionario = Funcionario.objects.filter(is_superuser=False).order_by('last_name')
        self.ctx['usuarios_list'] = funcionario
        return render(request, self.template_name, self.ctx)


class FuncionarioDetalle(View):
    template_name = 'funcionario/detalle.html'
    ctx = {}

    @method_decorator(permission_required('accounts.add_usuario'))
    def get(self, request, *args, **kwargs):
        usuario = get_object_or_404(Funcionario, id=int(kwargs['pk']))
        self.ctx['usuario'] = usuario
        return render(request, self.template_name, self.ctx)

    @method_decorator(permission_required('accounts.add_usuario'))
    def post(self, request, *args, **kwargs):
        usuario = get_object_or_404(Funcionario, id=int(kwargs['pk']))
        if request.POST['type'] == 'cod':
            CodigoUsuario.objects.create(
                id=request.POST['codigo'],
                funcionario=usuario
            )
            self.ctx['usuario'] = usuario
        else:
            Extension.objects.create(
                id=request.POST['codigo'],
                funcionario=usuario
            )
            self.ctx['usuario'] = usuario
        return render(request, self.template_name, self.ctx)
