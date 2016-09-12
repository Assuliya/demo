from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from ..login_reg.models import User
from models import Travel, Join
from datetime import date

def index(request):
    user = User.objects.get(id = request.session['user'])
    travels = Travel.objects.filter(user_id = request.session['user'])
    joins = Join.objects.filter(user_id = request.session['user'])
    other = Travel.objects.exclude(join_travel__user_id_id = request.session['user']).order_by('start')
    context = {'travels':travels, 'user':user, 'other':other, 'joins': joins}
    return render(request, 'travel_plan/index.html', context)

def travel(request, travel_id):
    travel = Travel.objects.get(id = travel_id)
    joins = Join.objects.filter(travel_id = travel_id)
    context = {'travel':travel, 'joins':joins}
    return render(request, 'travel_plan/travel.html', context)

def add(request):
    today = date.today()
    format_time = today.strftime('%Y-%m-%d')
    context = {'time':format_time}
    return render(request, 'travel_plan/add.html', context)

def add_travel(request):
    errors = []
    print request.POST['end']
    if len(request.POST['destination']) < 1:
        errors.append('Destination can not be empty')
    if len(request.POST['plan']) < 1:
        errors.append('Description can not be empty')
    if len(request.POST['start']) < 1:
        errors.append('Travel Date From can not be empty')
    if len(request.POST['end']) < 1:
        errors.append('Travel Date To can not be empty')
    if request.POST['end'] < request.POST['start']:
        errors.append('Travel Date To can not be earlier than Travel Date From')
    if len(errors) > 0:
        print errors
        print_messages(request, errors)
        return redirect(reverse('add'))
    creator = User.objects.get(id = request.session['user'])
    travel = Travel.objects.create(user_id = creator, destination=request.POST['destination'], plan=request.POST['plan'], start=request.POST['start'], end=request.POST['end'])
    return redirect(reverse('travel_index'))

def join(request, travel_id):
    user = User.objects.get(id = request.session['user'])
    travel = Travel.objects.get(id = travel_id)
    join = Join.objects.create(travel_id = travel, user_id = user)
    return redirect(reverse('travel_index'))
