from django.contrib.auth.models import AnonymousUser
from .models import Menu


def menus(request):
    data = {}
    if request.user == AnonymousUser():
        return {}
    elif request.user.is_superuser:
        data = Menu.objects.filter(superusuario=True).filter(padre=None)
    else:
        data = Menu.objects.filter(superusuario=False).filter(padre=None)

    return {'menu_list': getmenu(data)}


def getmenu(data):
    response = []
    for menu in data:
        dicmenu = {}
        dicmenu['nombre'] = menu.nombre
        dicmenu['url'] = menu.direccion
        dicmenu['icon'] = menu.icon
        dicmenu['color'] = menu.color
        if menu.hijos.all() is None:
            dicmenu['hijos'] = False
        else:
            dicmenu['hijos'] = getmenu(menu.hijos.all())
        response.append(dicmenu)

    return response
