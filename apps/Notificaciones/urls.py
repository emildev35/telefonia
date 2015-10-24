from django.conf.urls import patterns, url
from .views import visto, ShowAllView

urlpatterns = patterns(
    '',
    url(r'^clean$', visto, name='clean_notifications'),
    url(r'^$', ShowAllView, name='all_notifications'),
)
