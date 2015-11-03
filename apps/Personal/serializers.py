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
    class Meta:
        model = Funcionario
