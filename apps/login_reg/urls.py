from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='log_index'),
    url(r'login$', views.login_process, name='log_login'),
    url(r'register$', views.register_process, name='log_register'),
    url(r'success$', views.success, name='log_success'),
    url(r'logout$', views.logout, name='log_logout'),
    url(r'delete/(?P<user_id>\d+)$', views.delete, name='log_delete')
]
