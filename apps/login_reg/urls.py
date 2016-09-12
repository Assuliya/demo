from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='log_index'),
    url(r'user/edit/(?P<user_id>\d+)$', views.edit, name='log_edit'),
    url(r'user/deletion_page$', views.deletion_page, name='log_deletion_page'),

    url(r'login$', views.login_process, name='log_login'),
    url(r'register$', views.register_process, name='log_register'),
    url(r'success$', views.success, name='log_success'),
    url(r'logout$', views.logout, name='log_logout'),

    url(r'user/(?P<user_id>\d+)/update$', views.update, name='log_update'),
    url(r'user/(?P<user_id>\d+)/update_pass$', views.update_pass, name='log_update_pass'),
    url(r'^user/(?P<user_id>\d+)/delete$', views.delete, name='log_delete'),


]
