from .models import WHO_Set2_Weight_For_Length_Male, WHO_Set2_BMI_Female, WHO_Set2_Head_Circumference_Male, WHO_Set2_Head_Circumference_Female
from django.core import serializers

def get_standard_curves():
  #TODO Complete this
  weight_for_length_male_sc = WHO_Set2_Weight_For_Length_Male.objects.all()
  weight_for_length_male_json_sc = serializers.serialize("json", weight_for_length_male_sc)
  
  bmi_female_sc = WHO_Set2_BMI_Female.objects.all()
  bmi_female_json_sc = serializers.serialize("json", bmi_female_sc)
  
  head_circumference_male_sc =  WHO_Set2_Head_Circumference_Male.objects.all()
  head_circumference_male_json_sc = serializers.serialize("json", head_circumference_male_sc)

  head_circumference_female_sc =  WHO_Set2_Head_Circumference_Female.objects.all()
  head_circumference_female_json_sc = serializers.serialize("json", head_circumference_female_sc)
  
  return weight_for_length_male_json_sc
