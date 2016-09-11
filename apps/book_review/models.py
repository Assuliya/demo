from __future__ import unicode_literals
from django.db import models
from ..login_reg.models import User


class Book(models.Model):
      title = models.CharField(max_length=255)
      author = models.CharField(max_length=255)
      user_id = models.ForeignKey(User, related_name='book_to_user')
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
      review = models.TextField(max_length=1000)
      rating = models.PositiveSmallIntegerField()
      user_id = models.ForeignKey(User, related_name='review_to_user')
      book_id = models.ForeignKey(Book, related_name='review_to_book')
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
