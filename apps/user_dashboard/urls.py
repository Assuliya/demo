from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard_dashboard'),
    url(r'^user/(?P<user_id>\d+)$', views.show, name='dashboard_show'),
    url(r'^user/(?P<page_id>\d+)/add_message$', views.add_message, name='dashboard_add_message'),
    url(r'^user/(?P<message_id>\d+)/add_comment$', views.add_comment, name='dashboard_add_comment')

]
