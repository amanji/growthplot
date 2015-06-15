from .models import WHO_Set2_Weight_For_Length_Male, WHO_Set2_BMI_Female, WHO_Set2_Head_Circumference_Male, WHO_Set2_Head_Circumference_Female, Parent
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

def verify_registration(request):
  # TODO:
  email = request.POST['email']
  password = request.POST['password']
  confirm_password = request.POST['confirm-password']
  
  if (email == ''):
    return "You must enter a valid email"

  if (password == '' or confirm_password == ''):
    return "You must enter a password"

  if (password != confirm_password):
    return "Paswords do not match"

  # Otherwise all fields entered correctly, check database that user doesnt exist
  else:
    user_exists = Parent.objects.filter(email=email)
    if user_exists:
      return "That user is already in the database"
    else:
      user = Parent(email=email, password=password)
      user.save()
  
  return None


def login_user(request):
  email = request.POST['email']
  password = request.POST['password']

  if (email == ''):
    return "You must enter a valid email"

  if (password == ''):
    return "You must enter a password"

  else:
    user_exists = Parent.objects.get(email=email)
    if not user_exists:
      return "That user does not exist, please regigster."
    elif user_exists.password != password:
        return "You have entered an invalid password"
    else:
        return None