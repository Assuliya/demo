from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from ..login_reg.models import User
from models import Message, Comment


def dashboard(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'user_dashboard/dashboard.html', context)

def show(request, user_id):
    if not 'user' in request.session:
        return redirect(reverse('index'))
    user = User.manager.get(id=user_id)
    messages = Message.objects.filter(user_id_to=user_id)
    comments = Comment.objects.all()
    context = {'user':user, 'messages':messages, 'comments': comments}
    return render(request, 'user_dashboard/show.html', context)

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
