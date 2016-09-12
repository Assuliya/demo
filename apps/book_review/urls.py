from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='books_index'),
    url(r'books/add$', views.add, name='books_add'),
    url(r'user/(?P<user_id>\d+)$', views.user, name='books_user'),
    url(r'books/(?P<book_id>\d+)$', views.specific, name='books_specific'),
    url(r'^books/add_book$', views.add_book, name='books_add_book'),
    url(r'^books/(?P<book_id>\d+)/add_review$', views.add_review, name='books_add_review'),
    url(r'^reviews/(?P<review_id>\d+)/delete$', views.delete_review, name='books_delete_review')

]
