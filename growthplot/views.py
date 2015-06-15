from django.http import HttpResponse
from django.template import RequestContext, loader
import controllers as controllers
from django.shortcuts import render

def index(request):
    curve = controllers.get_standard_curves()
    return render(request, 'index.html', {'weight_for_length_male' : curve})

def login(request):
  if request.method == 'GET': 
    return render(request, 'login.html')
  elif request.method == 'POST':
    message = controllers.login_user(request)
    if message:
      return render(request, 'login.html', {'message' : message})
    else: 
      return render(request, 'index.html', {})

def register(request):
  if request.method == 'GET':
    return render(request, 'register.html')
  elif request.method == 'POST':
    message = controllers.verify_registration(request)
    if message:
      return render(request, 'register.html', {'message' : message})
    else:
      return render(request, 'login.html', {})