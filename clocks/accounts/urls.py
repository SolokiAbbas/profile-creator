from django.conf.urls import url
from accounts import views

app_name = 'accounts'

urlpatterns = [
    url(r'^register', views.register, name='register'),
    url(r'^user_login/', views.user_login, name='user_login'),
    url(r'^profile_detail/$', views.current_user, name='profile_detail'),

]
