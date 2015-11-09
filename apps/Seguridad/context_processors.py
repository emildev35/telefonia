from django.contrib.auth.models import AnonymousUser
from .models import Menu


def menus(request):
    data = {}
    if request.user == AnonymousUser():
        return {}
    else:
        data = Menu.objects.filter(funcionario=request.user, padre=None)
    return {'menu_list': getmenu(data)}


def getmenu(data):
    response = []
    for menu in data:
        dicmenu = {}
        dicmenu['nombre'] = menu.descripcion
        dicmenu['url'] = menu.url
        dicmenu['icon'] = menu.icon
        dicmenu['color'] = menu.color
        if menu.hijos.all() is None:
            dicmenu['hijos'] = False
        else:
            dicmenu['hijos'] = getmenu(menu.hijos.all())
        response.append(dicmenu)

    return response
