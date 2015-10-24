import random
from django_ajax.decorators import ajax
from .models import CodigoProyecto


@ajax
def generarCodigo(request):
    codigos = CodigoProyecto.objects.values_list('id').all()
    data = [x[0] for x in codigos]
    while True:
        new_code = random.randint(100000, 999999)
        if new_code in data:
            continue
        else:
            return new_code
