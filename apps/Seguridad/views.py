from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout


def loginview(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=usuario, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('accounts_home'))
            else:
                return render(request, 'seguridad/login.html', {'message': 'USUARIO NO ACTIVO'})
        else:
            return render(request, 'seguridad/login.html', {'message': 'USUARIO O PASSWORD INCORECTO'})
    else:
        return render(request, 'seguridad/login.html', {})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('seguridad_login'))
