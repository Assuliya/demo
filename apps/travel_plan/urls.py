from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='travel_index'),
    url(r'^travels/destination/(?P<travel_id>\d+)$', views.travel, name='travel_travel'),
    url(r'^travels/add$', views.add, name='travel_add'),
    url(r'^travels/add_travel$', views.add_travel, name='travel_add_travel'),
    url(r'^travels/(?P<travel_id>\d+)/join$', views.join, name='travel_join'),

]
