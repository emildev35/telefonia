import decimal
import datetime
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from suds.client import Client
from pytz import timezone
from apps.Reportes.models import ConfiguracionCuenta
from .models import Usuario, Unidad, CodigoProyecto


@periodic_task(run_every=crontab(day_of_month='1'))
def test():
    configuracion = ConfiguracionCuenta()
    configuracion.montoDisponible = decimal.Decimal(30.00)
    configuracion.activo = True
    configuracion.save()

# -*- coding: utf-8 -*-
lpz = timezone('America/La_Paz')


@periodic_task(run_every=crontab(hour="*/10", minute="*", day_of_week="*"))
def UpdateUsers():
    """ Actualizacion periodica de los usarios de la base de datos mediante
    WebServices
    direccion http://172.16.0.8/Services/services/Srrhh/SRecursos.asmx
    """
    url = 'http://172.16.0.8/Services/services/Srrhh/SRecursos.asmx?WSDL'
    wsclient = Client(url)
    Funcionarios = wsclient.service.DatosFuncionario('01-01-1999')
    Funcionarios = Funcionarios['Funcionarios']
    unidad = Unidad.objects.get(id=1)
    nickexistentes = []
    for i in Funcionarios:
        if i['Usuario'] is None:
            continue
        nickexistentes.append(formatutf8(i['Usuario']))

    for i in Funcionarios:
        if i['Usuario'] is None:
            i['Usuario'] = generatenick(formatutf8(
                formatutf8(i['Nombre'])),
                nickexistentes
                )
            nickexistentes.append(i['Usuario'])

    for Funcionario in Funcionarios:
        if Funcionario['Estado'] == '1':
            if not Funcionario['Usuario'] is None:
                fechaMod = datetime.datetime.strptime(
                    Funcionario['FechaModificacion'],
                    '%Y/%m/%d %I:%M:%S'
                )
                try:
                    usuario = Usuario.objects.get(
                        username=formatutf8(Funcionario['Usuario'])
                        )
                except Usuario.DoesNotExist:
                    usuario = None

                if usuario is None:
                    fullname = get_names(Funcionario['Nombre'])
                    usuario = Usuario.objects.create_user(
                        formatutf8(Funcionario['Usuario']),
                        Funcionario['Mail'],
                        Funcionario['Pin']
                        )
                    usuario.unidad = unidad
                    usuario.ip = Funcionario['Ip']
                    if not fullname[1] is None:
                        usuario.first_name = formatutf8(fullname[0])
                        usuario.last_name = formatutf8(fullname[1])
                    else:
                        usuario.default_name = formatutf8(fullname[0])
                    usuario.oficina = formatutf8(Funcionario['Oficina'])
                    usuario.idOficina = Funcionario['IdOficina']
                    usuario.cargo = formatutf8(Funcionario['Cargo'])
                    usuario.fotografia = Funcionario['Foto']
                    usuario.activo = True
                    fechaNac = datetime.datetime.strptime(
                        Funcionario['FechaModificacion'],
                        '%Y/%m/%d %I:%M:%S'
                    )
                    usuario.fechaNacimiento = fechaNac
                    usuario.fechaModificacion = fechaMod
                    usuario.ci = Funcionario['Documento']
                    usuario.save()
                    pinUsuario = CodigoProyecto()
                    pinUsuario.id = Funcionario['Pin']
                    pinUsuario.activo = True
                    pinUsuario.usuario = usuario
                    pinUsuario.save()
                else:
                    if usuario.fechaModificacion < lpz.localize(fechaMod):
                        fullname = get_names(Funcionario['Nombre'])
                        usuario.unidad = unidad
                        usuario.ip = Funcionario['Ip']
                        if not fullname[1] is None:
                            usuario.first_name = formatutf8(fullname[0])
                            usuario.last_name = formatutf8(fullname[1])
                        else:
                            usuario.default_name = formatutf8(fullname[0])
                        usuario.set_password(Funcionario['Pin'])
                        usuario.oficina = formatutf8(Funcionario['Oficina'])
                        usuario.idOficina = Funcionario['IdOficina']
                        usuario.ci = Funcionario['Documento']
                        usuario.cargo = formatutf8(Funcionario['Cargo'])
                        usuario.activo = True
                        usuario.fechaModificacion = fechaMod
                        usuario.fotografia = Funcionario['Foto']
                        usuario.ci = Funcionario['Documento']
                        usuario.save()
                        pinUsuario = CodigoProyecto()
                        pinUsuario.id = Funcionario['Pin']
                        pinUsuario.activo = True
                        pinUsuario.usuario = usuario
                        pinUsuario.save()


def formatutf8(data):
    if data is None:
        return None
    return unicode(str(data.encode('utf8')), 'utf-8')


def generatenick(firtname, usuarios):
    """Funcion encargada de devolver el nick
    de un funcionario

    :firtname: nombre completo de funcionario
    :usuario: lista de los usuario registrados
    :returns: usuario para un funcionario

    """
    num = 1
    while True:
        names = firtname.split(' ')
        if len(names) == 5:
            usuario = formatutf8(names[0][0:num])
            usuario = formatutf8(names[3] + formatutf8(names[4]))
        if len(names) == 4:
            usuario = formatutf8(names[0][0:num]) + formatutf8(names[2])
        elif len(names) == 3:
            usuario = formatutf8(names[0][0:num]) + formatutf8(names[1])
        elif len(names) == 2:
            usuario = formatutf8(names[0][0:num]) + formatutf8(names[1])
        else:
            return None
        if usuario.lower() in usuarios:
            num += 1
        else:
            return usuario.lower()


def get_names(firtname):
    """Funcion encargada de devolver los nombres y apellidos
    de un funcionario

    :firtname: nombre completo de funcionario
    :returns: [first_name, last_name]
    """
    names = firtname.split(' ')
    if len(names) == 4:
        first_name = formatutf8(names[0]) + ' ' + formatutf8(names[1])
        last_name = formatutf8(names[2]) + ' ' + formatutf8(names[3])
        return [first_name, last_name]
    elif len(names) == 3:
        first_name = formatutf8(names[0])
        last_name = formatutf8(names[1]) + ' ' + formatutf8(names[2])
        return [first_name, last_name]
    elif len(names) == 2:
        first_name = formatutf8(names[0])
        last_name = formatutf8(names[1])
        return [first_name, last_name]
    elif len(names) > 5:
        return [firtname, None]
    return [firtname, None]
