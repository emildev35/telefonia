from django.http import HttpResponseRedirect
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import logout


class IpAccessMiddleware(object):

    def process_request(self, request):
        usuario = request.user
        if request.user == AnonymousUser():
            pass
        else:
            if str(usuario.ip) == str(request.META['REMOTE_ADDR']):
                pass
            else:
                logout(request)
                return HttpResponseRedirect('/')
