from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from ..login_reg.models import User
from models import Message, Comment
import bcrypt


def index(request):
    return render(request, 'user_dashboard/index.html')

def show(request, user_id):
    if not 'user' in request.session:
        return redirect(reverse('index'))
    user = User.manager.get(id=user_id)
    messages = Message.objects.filter(user_id_to=user_id)
    comments = Comment.objects.all()
    context = {'user':user, 'messages':messages, 'comments': comments}
    return render(request, 'user_dashboard/show.html', context)

def edit(request, user_id):
    user = User.objects.get(id = user_id)
    context = {'user':user}
    return render(request, 'user_dashboard/edit.html', context)

def dashboard(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'user_dashboard/dashboard.html', context)

def deletion_page(request):
    return render(request, 'user_dashboard/delete.html')

def update(request, user_id):
    result = User.manager.validateReg(request)
    if result[0] == False:
        print_messages(request, result[1])
        return redirect(reverse('dashboard_edit', kwargs={'user_id':request.session['user']}))
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
        return redirect(reverse('dashboard_edit', kwargs={'user_id':request.session['user']}))
    pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    update = User.objects.get(id = user_id)
    update.pw_hash = pw_hash
    update.save(update_fields=None)
    return redirect(reverse('dashboard_show', kwargs={'user_id':request.session['user']}))

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.ERROR, message)

def delete(request, user_id):
    User.manager.delete(user_id)
    request.session.pop('user')
    return redirect('/')

def add_message(request, page_id):
    if request.method == "POST":
        user = User.objects.get(id=request.session['user'])
        page = User.objects.get(id=page_id)
        Message.objects.create(message = request.POST['message'], user_id = user, user_id_to = page)
        return redirect(reverse('dashboard_show', kwargs={'user_id':page_id}))
    else:
	    return redirect(reverse('dashboard_show'))

def add_comment(request, message_id):
    if request.method == "POST":
        user = User.objects.get(id=request.session['user'])
        message = Message.objects.get(id=message_id)
        page = message.user_id_to.id
        Comment.objects.create(comment = request.POST['comment'], user_id = user, message_id = message)
        return redirect(reverse('dashboard_show', kwargs={'user_id':page}))
    else:
	    return redirect(reverse('dashboard_show'))
