from rest_framework import serializers
from .models import Cargo, Area, Funcionario


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ('id', 'descripcion', 'fechaRegistro')


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ('id', 'descripcion', 'fechaRegistro')


class FuncionarioSerializer(serializers.ModelSerializer):
    cargo = CargoSerializer().fields['descripcion']
    area = AreaSerializer().fields['descripcion']

    class Meta:
        model = Funcionario
        fields = ('id', 'first_name', 'last_name', 'username', 'fecha_nacimiento', 'ci', 'ip', 'cargo', 'area', 'fotografia')
