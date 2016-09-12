from __future__ import unicode_literals
from django.db import models
from ..login_reg.models import User

class Message(models.Model):
      message = models.TextField(max_length=1000)
      user_id_to = models.ForeignKey(User, related_name='to_user')
      user_id = models.ForeignKey(User, related_name='from_user')
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
      comment = models.TextField(max_length=1000)
      user_id = models.ForeignKey(User)
      message_id = models.ForeignKey(Message)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
