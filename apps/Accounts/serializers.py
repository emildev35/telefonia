from rest_framework import serializers
from .models import Extension
from apps.Personal.serializers import FuncionarioSerializer


class ExtensionSerializer(serializers.ModelSerializer):
    funcionario = FuncionarioSerializer().fields['username']

    class Meta:
        model = Extension
        fields = ('id', 'fecha_registro', 'funcionario')
