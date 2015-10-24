import decimal
from .models import Alerta
from apps.Reportes.models import Cuenta


def calcularCuenta(usuario, costo):
    cuenta = Cuenta.objects.filter(usuario=usuario, activo=True)[0]
    cuenta.monto -= costo
    cuenta.save()
    if cuenta.monto < decimal.Decimal(10.000):
        alerta = Alerta(usuario=usuario, cuerpo='Error', tipo='danger')
        alerta.save()


def insertarAlerta(usuario, mensaje, tipo):
    alerta = Alerta(usuario=usuario, cuerpo=mensaje, tipo=tipo)
    alerta.save()
