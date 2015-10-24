import decimal
from .models import ConfiguracionCuenta


def crear_cuentas():
    configuracion = ConfiguracionCuenta()
    configuracion.montoDisponible = decimal.Decimal(30.00)
    configuracion.activo = True
    configuracion.save()
