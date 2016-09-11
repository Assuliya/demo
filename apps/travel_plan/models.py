from __future__ import unicode_literals
from django.db import models
from ..login_reg.models import User

class Travel(models.Model):
      destination = models.CharField(max_length=255)
      plan = models.TextField(max_length=500)
      start = models.DateField()
      end = models.DateField()
      user_id = models.ForeignKey(User, related_name='travel_create')
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

class Join(models.Model):
      travel_id = models.ForeignKey(Travel, related_name='join_travel')
      user_id = models.ForeignKey(User, related_name='join_user')
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
