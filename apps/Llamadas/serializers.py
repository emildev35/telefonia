from rest_framework import serializers
from .models import Cdr
from apps.Accounts.serializers import ExtensionSerializer


class CdrSerializer(serializers.ModelSerializer):
    src = ExtensionSerializer()
    dst = ExtensionSerializer()

    class Meta:
        model = Cdr
        fields = ('accid', 'calldate', 'src', 'dst', 'billsec', 'duration', 'disposition')
        read_only_fields = ('src', 'dst')
