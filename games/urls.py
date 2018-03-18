from django.conf.urls import url
from games import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'games'

urlpatterns = [
    url(r'^forced/$', views.forced, name='forced'),
    url(r'^wave/$', views.wave, name='wave'),
    url(r'^particle/$', views.particle, name='particle')
]

urlpatterns += staticfiles_urlpatterns()
