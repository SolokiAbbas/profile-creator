from django.conf.urls import url
from games import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'games'

urlpatterns = [
    url(r'^forced/$', views.forced, name='forced'),
    url(r'^collision/$', views.collision, name='collision'),
    url(r'^fireball/$', views.fireball, name='fireball')
]

urlpatterns += staticfiles_urlpatterns()
