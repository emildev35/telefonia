from django.views.generic.edit import CreateView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from django.core.urlresolvers import reverse_lazy
from .models import Cargo, Area
from .serializers import CargoSerializer, AreaSerializer


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
