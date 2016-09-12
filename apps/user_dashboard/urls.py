from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='dashboard_index'),
    url(r'user/(?P<user_id>\d+)/edit$', views.edit, name='dashboard_edit'),
    url(r'user/dashboard$', views.dashboard, name='dashboard_dashboard'),
    url(r'^user/(?P<user_id>\d+)$', views.show, name='dashboard_show'),
    url(r'user/deletion_page$', views.deletion_page, name='dashboard_deletion_page'),


    url(r'user/(?P<user_id>\d+)/update$', views.update, name='dashboard_update'),
    url(r'user/(?P<user_id>\d+)/update_pass$', views.update_pass, name='dashboard_update_pass'),
    url(r'^user/(?P<user_id>\d+)/delete$', views.delete, name='dashboard_delete'),

    url(r'^user/(?P<page_id>\d+)/add_message$', views.add_message, name='dashboard_add_message'),
    url(r'^user/(?P<message_id>\d+)/add_comment$', views.add_comment, name='dashboard_add_comment')

]
