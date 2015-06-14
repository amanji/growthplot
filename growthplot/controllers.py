from .models import WHO_Set2_Weight_For_Length_Male
from django.core import serializers


def get_standard_curves():
  weight_for_length_male_sc = WHO_Set2_Weight_For_Length_Male.objects.all()
  return serializers.serialize("json", weight_for_length_male_sc)
