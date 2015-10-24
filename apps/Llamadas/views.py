import datetime as dt
import decimal
import csv
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist
from django_ajax.response import JSONResponse
from apps.utils.db import procedure
from apps.Notificaciones.tasks import insertarAlerta, calcularCuenta
from .models import Tarifa, Horario, DescripcionLlamada, CodigoProyecto
from .models import Llamada, Region


class HomeView(TemplateView):
    template_name = 'llamadas/home.html'


class TarifaView(View):
    template_name = 'llamadas/tarifa/home.html'
    @method_decorator(permission_required('llamadas.add_tarifa'))
    def get(self, request):
        tarifas = Tarifa.objects.filter(activo=True).order_by('tipo', 'zona')
        return render(request, self.template_name, {'tarifas': tarifas})
    @method_decorator(permission_required('llamadas.add_tarifa'))
    def post(self, request):
        tipo = request.POST['tipo']
        zona = request.POST['zona']
        precio = request.POST['precio']
        tarifa = Tarifa(tipo=tipo, zona=zona, precio=precio, activo=True)
        tarifa.save()
        alerta = {'data': 'TARIFA MODIFICADA CON EXITO', 'tipo': 'success'}
        tarifas = Tarifa.objects.filter(activo=True).order_by('tipo', 'zona')
        return render(request, self.template_name, {
            'tarifas': tarifas,
            'alerta': alerta
            })


class HorarioView(View):
    template_name = 'llamadas/horario.html'
    @method_decorator(permission_required('llamadas.add_horario'))
    def get(self, request):
        horario = Horario.objects.filter(activo=True)[0]
        return render(request, self.template_name, {'horario': horario})
    @method_decorator(permission_required('llamadas.add_horario'))
    def post(self, request):
        ingreso = [
            x.strip().replace(' ', '')
            for x in request.POST["horaIngreso"].split(':')
        ]
        ingresoTarde = [
            x.strip().replace(' ', '')
            for x in request.POST["horaIngresoTarde"].split(':')
        ]
        jornada = [
            x.strip().replace(' ', '')
            for x in request.POST["jornada"].split(':')
        ]
        jornada = dt.timedelta(hours=int(jornada[0]), minutes=int(jornada[1]))
        ingreso = dt.time(int(ingreso[0]), int(ingreso[1]))
        ingresoTarde = dt.time((int(ingresoTarde[0])+12), int(ingresoTarde[1]))
        horario = Horario.objects.create(
            horaIngreso=ingreso,
            horaIngresoTarde=ingresoTarde,
            tiempoJornada=jornada
            )
        if horario:
            alerta = {
                'tipo': 'success',
                'data': 'OPERACION REALIZADA CON EXITO'
                }
        else:
            alerta = {
                'tipo': 'danger',
                'data': 'OCURIO UN ERROR'
                }
        return render(request, self.template_name, {
            'horario': horario,
            'alerta': alerta
            })


class ImportarDatosView(View):
    template_name = 'llamadas/import_data.html'
    @method_decorator(permission_required('llamadas.add_llamada'))
    def get(self, request):
        return render(request, self.template_name, {})
    @method_decorator(permission_required('llamadas.add_llamada'))
    def post(self, request):
        cvsfile = request.FILES['archivo']
        records = csv.reader(cvsfile)
        alertas = []
        for llamada in records:
            if llamada[0][0] != 'F':
                llamada = llamada[0].split(';')
                tiempo = dt.datetime.strptime(llamada[0], '%d/%m/%Y %H:%M:%S')
                fecha = tiempo.date()
                hora = tiempo.time()
                numero_origen = llamada[4]
                numero_marcado = llamada[5]
                tarifa = decimal.Decimal(0.00000)
                duracion_enlace = llamada[6]
                duracion_llamada = llamada[7]
                numero = ''
                tipo_llamada = llamada[8]
                codigo_proyecto = llamada[10]
                interno = llamada[2]
                tiempoEspera = [int(x) for x in duracion_llamada.split(':')]
                duracion = [int(x) for x in duracion_enlace.split(':')]
                duracion = dt.timedelta(
                    hours=duracion[0],
                    minutes=duracion[1],
                    seconds=duracion[2]
                )
                tiempoEspera = dt.timedelta(
                    hours=tiempoEspera[0],
                    minutes=tiempoEspera[1],
                    seconds=tiempoEspera[2]
                )
                if codigo_proyecto == '':
                    codigo_proyecto = 2
                try:
                    codigoProyecto = CodigoProyecto.objects.get(
                        id=int(codigo_proyecto)
                    )
                    if tipo_llamada == 'entrante':
                        tipo_llamada = 'I'
                        numero = numero_origen
                        if numero == '':
                            numero = 'DESCONOCIDO'
                        tarifa = decimal.Decimal(0.00)
                    elif tipo_llamada == 'saliente':
                        tipo_llamada = 'O'
                        numero = numero_marcado
                        if len(numero) == 8:
                            if int(numero[0]) in (6, 7):
                                Z = 'L'
                                T = 'M'
                            else:
                                Z = 'N'
                                T = 'F'
                        elif len(numero) == 7:
                            Z = 'L'
                            T = 'F'
                        elif len(numero) == 9:
                            if '9011' in numero[0]:
                                tipo_llamada == 'E'
                            elif int(numero[1]) in (7, 6):
                                Z = 'N'
                                T = 'M'
                        elif len(numero) > 9:
                            tipo_llamada == 'E'
                        else:
                            pass
                        try:
                            tarifa = Tarifa.objects.filter(
                                tipo=T,
                                zona=Z,
                                activo=True
                            )[0]
                            tarifa = tarifa.precio
                        except ObjectDoesNotExist:
                            tarifa = decimal.Decimal(0.00)

                    region = Region.objects.get(id=1003)
                    horario = Horario.objects.filter(activo=True)[0]
                    costo = decimal.Decimal(duracion.seconds/60.0000)*tarifa
                    # Insercion de la Llamada
                    llamada = Llamada()
                    llamada.hora = hora
                    llamada.fecha = fecha
                    llamada.numeroInterno = interno
                    llamada.codigoProyecto = codigoProyecto
                    llamada.numero = numero
                    llamada.duracion = duracion
                    llamada.tiempoEspera = tiempoEspera
                    llamada.region = region
                    llamada.horario = horario
                    llamada.tipoLlamada = tipo_llamada
                    llamada.costo = costo
                    try:
                        llamada.save()
                        calcularCuenta(codigoProyecto.usuario, costo)
                        alerta = {
                            'type': 'success',
                            'message': 'LLAMADA REGISTRADA'
                        }
                    except:
                        insertarAlerta(
                            codigoProyecto.usuario,
                            'Se produjo un erro con la una llamada',
                            'danger'
                        )
                        alerta = {
                            'type': 'danger',
                            'message': 'LLAMADA DUPLICADA'
                        }
                    alertas.append(alerta)

                except ObjectDoesNotExist:
                    alerta = {
                        'type': 'danger',
                        'message': codigo_proyecto + ' NO ENCONTRADO'
                    }
                    alertas.append(alerta)


class LlamadasView(View):
    template_name = 'llamadas/llamada/home.html'
    @method_decorator(permission_required('llamadas.add_llamada'))
    def get(self, request):
        return render(request, self.template_name, {})


class LlamadasUsuarioView(View):
    template_name = 'llamadas/llamada/usuario.html'
    @method_decorator(permission_required('llamadas.add_llamada'))
    def get(self, request):
        return render(request, self.template_name, {})


class LlamadasOficinaView(View):
    template_name = 'llamadas/llamada/oficina.html'
    @method_decorator(permission_required('llamadas.add_llamada'))
    def get(self, request):
        return render(request, self.template_name, {})


class LlamadasPersonalesView(View):
    template_name = 'llamadas/llamada/personales.html'

    def get(self, request):
        llamadas_list = procedure('llamadas_usuario', request.user.id)
        paginator = Paginator(llamadas_list, 25)
        page = request.GET.get('page')
        try:
            llamadas = paginator.page(page)
        except PageNotAnInteger:
            llamadas = paginator.page(1)
        except EmptyPage:
            llamadas = paginator.page(paginator.num_pages)

        if page is None:
            page = 1

        if int(page) > 1:
            return render(
                request,
                'llamadas/llamada/cardscroll.html',
                {'llamadas': llamadas}
            )

        return render(request, self.template_name, {'llamadas': llamadas})

    def post(self, request):
        if request.POST['motivo'] == '':
            return JSONResponse(
                {'mensaje': 'El campo de motivo no debe estar vacio!'}
                )
        else:
            ds_llamada = DescripcionLlamada.objects.get(id=request.POST['id'])
            if ds_llamada:

                ds_llamada.registrado = True
                ds_llamada.nombre = 'L'
                ds_llamada.motivo = request.POST['motivo']
                ds_llamada.save()
            else:
                return JSONResponse({'mensaje': 'ERROR DEL SISTEMA'})
            return JSONResponse({})
