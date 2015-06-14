from django.http import HttpResponse
from django.template import RequestContext, loader
import controllers as controllers

def index(request):
    curve = controllers.get_standard_curves()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'weight_for_length_male' : curve}))

# def standard_curve_example(request):
#   #TODO: Change the standard curve variables so they are more intuitive
#   curve = controllers.get_standard_curves()
#   print curve
#   template = loader.get_template('sample_standard_curve.html')
#   return HttpResponse(template.render({'sc' : curve}))