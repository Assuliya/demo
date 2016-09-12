from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from models import User
from django.core.exceptions import ObjectDoesNotExist
import bcrypt

def index(request):
    return render(request, 'login_reg_app/index.html')

def success(request):
    return render(request, 'login_reg_app/success.html')

def register_process(request):
    result = User.manager.validateReg(request)
    resultPass = User.manager.validateRegPass(request)
    if result[0] == False or resultPass[0] == False:
        errors = result[1]+resultPass[1]
        print_messages(request, errors)
        return redirect(reverse('log_index'))
    pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.manager.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], username=request.POST['username'], pw_hash=pw_hash)
    return log_user_in(request, user)

def login_process(request):
    result = User.manager.validateLogin(request)
    if result[0] == False:
        print_messages(request, result[1])
        return redirect(reverse('log_index'))
    return log_user_in(request, result[1])

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.ERROR, message)

def log_user_in(request, user):
    request.session['user'] = user.id
    user.user_level = 1
    user.save(update_fields=None)
    return redirect(reverse('log_success'))

def logout(request):
    user = User.manager.get(id=request.session['user'])
    user.user_level = 0
    # user.check = 0
    user.save(update_fields=None)
    request.session.pop('user')
    return redirect(reverse('log_index'))

def delete(request, user_id):
    User.objects.delete(user_id)
    return redirect(reverse('log_index'))
