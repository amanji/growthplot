from django.http import HttpResponse
from django.template import RequestContext, loader
import controllers as controllers
from django.shortcuts import render, redirect

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import json

def index(request):
    return render(request, 'index.html', {})

def login(request):
  if request.method == 'GET': 
    return render(request, 'index.html', {})
  elif request.method == 'POST':
    message, user = controllers.get_profile(request)

    if not message and user:
      # loggedIn
      return redirect(profile)
    if message and not user:
      # wrong password
      return render(request, 'index.html', {'message' : message})
    if not message and not user:
      # user does not exist
      return render(request, 'register.html', {'message' : 'This user does not exist, please register'})

    # if message and user:
    #   return render(request, 'index.html', {'message' : message})
    # elif message and not user:
    #   return render(request, 'register.html', {'message' : message})
    # else: 
    #   return redirect(profile)

def logout_user(request):
  logout(request)
  return redirect('index')

def register(request):
  if request.method == 'GET':
    return render(request, 'register.html', {})
  elif request.method == 'POST':
    message = controllers.verify_registration(request)
    if message:
      return render(request, 'register.html', {'message' : message})
    else:
      return render(request, 'index.html', {})

@login_required
def profile(request):
  #Authenticate user
  children, children_json = controllers.get_children(request)
  if not children:
    info = "To begin using the system please register one or more children."
    return render(request, 'add_children.html', {'info' : info})
  else:
    return render(request, 'profile.html', {'children' : children, 'todays_date' : controllers.todays_date()})

@login_required()
def child(request):
  if request.method == 'GET':
    return render(request, 'add_children.html', {})
  elif request.method == 'POST':
    message = controllers.add_child(request)
    if message:
      return render(request, 'add_children.html', {'message' : message})
    else:
      return redirect(profile)

@login_required
def child_profile(request):
  if request.method == 'GET':
    return redirect(profile)
  elif request.method == 'POST':
    child_profile, log_entries = controllers.get_child_profile(request)
    return render(request, 'child_profile.html', {'child_profile' : child_profile, 'sex' : child_profile["sex"], 'less_than_2' : child_profile["less_than_2"], 'log_entries' : log_entries})

@login_required
#TODO:
def chart(request):
  if request.method == 'GET':
    return redirect(profile)
  elif request.method == 'POST':
    # Get chart data
    chart = controllers.chart(request)
    #chart_data = {'chart' : chart, 'standard_curve' : standard_curve,}
    return HttpResponse(chart, content_type = "application/json")

@login_required
def enter_log(request):
  if request.method == 'GET':
    return redirect(profile)
  elif request.method == 'POST':
    controllers.enter_log(request)
    return redirect(profile)