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
    return render(request, 'login.html', {})
  elif request.method == 'POST':
    message = controllers.get_profile(request)
    if message:
      return render(request, 'login.html', {'message' : message})
    else: 
      return redirect(profile)

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
      return render(request, 'login.html', {})

@login_required
def profile(request):
  #Authenticate user
  standard_curves = controllers.get_standard_curves()
  children, children_json = controllers.get_children(request)
  return render(request, 'profile.html', {'standard_curves' : standard_curves, 'children' : children, 'children_json' : children_json, 'todays_date' : controllers.todays_date()})

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
    child_profile, child_data = controllers.get_child_profile(request)
    return render(request, 'child_profile.html', {'child_profile' : child_profile, 'sex' : child_profile["sex"], 'less_than_2' : child_profile["less_than_2"], 'child_data' : child_data})

@login_required
#TODO: Set for deprecation - no longer needed
def data(request):
  if request.method == 'GET':
    return redirect(profile)
  elif request.method == 'POST':
    return None

@login_required
def enter_log(request):
  if request.method == 'GET':
    return redirect(profile)
  elif request.method == 'POST':
    controllers.enter_log(request)
    return redirect(profile)