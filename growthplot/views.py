from django.http import HttpResponse
import controllers as controllers

def index(request):
    curve = controllers.get_standard_curves()
    return HttpResponse(curve)