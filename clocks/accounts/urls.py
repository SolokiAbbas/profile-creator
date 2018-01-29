from django.conf.urls import url
from accounts import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'accounts'

urlpatterns = [
    url(r'^register', views.register, name='register'),
    url(r'^user_login/', views.user_login, name='user_login'),
    url(r'^profile_detail/$', views.update_profile, name='profile_detail'),
]

urlpatterns += staticfiles_urlpatterns()
