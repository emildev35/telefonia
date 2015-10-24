from celery import task


@task
def registarLlamada(args):
    descripcion = args
    descripcion.registrado = True
    descripcion.save()
