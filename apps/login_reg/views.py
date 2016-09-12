from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from models import User
from django.core.exceptions import ObjectDoesNotExist
import bcrypt

def index(request):
    if 'user' in request.session:
        return redirect(reverse('log_success'))
    return render(request, 'login_reg/index.html')

def success(request):
    user = User.objects.get(id = request.session['user'])
    context = {'user':user}
    return render(request, 'login_reg/success.html', context)

def edit(request, user_id):
    user = User.objects.get(id = user_id)
    context = {'user':user}
    return render(request, 'login_reg/edit.html', context)

def deletion_page(request):
    return render(request, 'login_reg/delete.html')

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
    return log_user_in(request, result[2])

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.ERROR, message)

def log_user_in(request, user):
    request.session['user'] = user.id
    user = User.manager.get(id=request.session['user'])
    user.user_level = 1
    user.save(update_fields=None)
    return redirect(reverse('log_success'))

def logout(request):
    user = User.manager.get(id=request.session['user'])
    # user.user_level = 0
    user.save(update_fields=None)
    request.session.pop('user')
    return redirect(reverse('log_index'))

def update(request, user_id):
    result = User.manager.validateReg(request)
    if result[0] == False:
        print_messages(request, result[1])
        return redirect(reverse('log_edit', kwargs={'user_id':request.session['user']}))
    update = User.objects.get(id = user_id)
    update.first_name = request.POST['first_name']
    update.last_name = request.POST['last_name']
    update.email = request.POST['email']
    update.username = request.POST['username']
    update.check = request.POST['check']
    update.save(update_fields=None)
    return redirect(reverse('dashboard_show', kwargs={'user_id':request.session['user']}))

def update_pass(request, user_id):
    result = User.manager.validateRegPass(request)
    result2 = User.manager.validateLogin(request)
    if result[0] == False or result2[0] == False:
        if result2[0] != False:
            print_messages(request, result[1])
        else:
            print_messages(request, result2[1])
        return redirect(reverse('log_edit', kwargs={'user_id':request.session['user']}))
    pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    update = User.objects.get(id = user_id)
    update.pw_hash = pw_hash
    update.save(update_fields=None)
    return redirect(reverse('dashboard_show', kwargs={'user_id':request.session['user']}))

def delete(request, user_id):
    User.manager.delete(user_id)
    request.session.pop('user')
    return redirect('/')
