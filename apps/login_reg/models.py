from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import bcrypt, re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASS_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')

class UserManager(models.Manager):
    def validateReg(self, request):
        errors = []
        if len(request.POST['first_name']) < 2:
            errors.append('First Name can not be less than 2 characters')
        elif not all(x.isalpha() or x.isspace() for x in request.POST['first_name']):
            errors.append('First Name should only contain letters')

        if len(request.POST['last_name']) < 2:
            errors.append('Last Name can not be less than 2 characters')
        elif not all(x.isalpha() or x.isspace() for x in request.POST['last_name']):
            errors.append('Last Name should only contain letters')

        if len(request.POST['username']) < 3:
            errors.append('Username can not be less than 3 characters')
        try:
            user = User.objects.get(username = request.POST['username'])
            errors.append('This Username is already being used')
        except ObjectDoesNotExist:
            pass

        if len(request.POST['email']) < 1:
            errors.append('Email can not be empty')
        elif not EMAIL_REGEX.match(request.POST['email']):
            errors.append('Email is not valid')
        try:
            user = User.objects.get(email = request.POST['email'])
            errors.append('This email is already being used')
        except ObjectDoesNotExist:
            pass

        if len(errors) > 0:
            return (False, errors)
        return (True, errors)


    def validateRegPass(self, request):
        errors = []
        if len(request.POST['password']) < 1:
            errors.append('Password can not be empty')
        elif len(request.POST['password']) < 8:
            errors.append('Password should be more than 7 characters')
        elif not PASS_REGEX.match(request.POST['password']):
            errors.append('Password should contain at least one apper case letter and one number')
        if request.POST['password'] != request.POST['repeat']:
            errors.append('Password repeat did not match the password')
        if len(errors) > 0:
            return (False, errors)
        return (True, errors)



    def validateLogin(self, request):
        from bcrypt import hashpw, gensalt
        errors = []
        try:
	        user = User.objects.get(email=request.POST['email'])
	        password = user.pw_hash.encode()
	        loginpass = request.POST['password'].encode()
	        if hashpw(loginpass, password) == password:
	            return (True, user)
	        else:
	            errors.append("Sorry, no password match")
	            return (False, errors)
        except ObjectDoesNotExist:
            pass
        errors.append("Sorry, no email found. Please try again.")
        return (False, errors)

    def delete(self, user_id):
        User.objects.filter(id = user_id).delete()

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    pw_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = models.Manager()
    manager = UserManager()
