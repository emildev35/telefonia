from .models import Funcionario


def addpass():
    for usuario in Funcionario.objects.all():
        usuario.set_password(usuario.username)
        usuario.save()
