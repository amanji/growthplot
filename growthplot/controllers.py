from .models import WHO_Set2_Weight_For_Length_Male, WHO_Set2_Weight_For_Length_Female
from .models import WHO_Set2_BMI_Male, WHO_Set2_BMI_Female
from .models import WHO_Set2_Head_Circumference_Male, WHO_Set2_Head_Circumference_Female
from .models import WHO_Set2_Weight_For_Age_Male, WHO_Set2_Weight_For_Age_Female
from .models import WHO_Set2_Height_For_Age_Male, WHO_Set2_Height_For_Age_Female
from .models import WHO_Set2_Length_For_Age_Male, WHO_Set2_Length_For_Age_Female
from .models import Parent, Child, Log_Entry
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import time
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import json

def get_standard_curves():
  standard_curves = {
    'weight_for_length_male_sc' : serializers.serialize("json", WHO_Set2_Weight_For_Length_Male.objects.all()),
    'weight_for_length_female_sc' : serializers.serialize("json", WHO_Set2_Weight_For_Length_Female.objects.all()),

    'bmi_female_sc' : serializers.serialize("json", WHO_Set2_BMI_Female.objects.all()),
    'bmi_male_sc' : serializers.serialize("json", WHO_Set2_BMI_Female.objects.all()),

    'head_circumference_male_sc' :  serializers.serialize("json", WHO_Set2_Head_Circumference_Male.objects.all()),
    'head_circumference_female_sc' :  serializers.serialize("json", WHO_Set2_Head_Circumference_Female.objects.all()),

    'weight_for_age_male_sc' : serializers.serialize("json", WHO_Set2_Weight_For_Age_Male.objects.all()),
    'weight_for_age_female_sc' : serializers.serialize("json", WHO_Set2_Weight_For_Age_Female.objects.all()),

    'height_for_age_male_sc' : serializers.serialize("json", WHO_Set2_Height_For_Age_Male.objects.all()),
    'height_for_age_female_sc' : serializers.serialize("json", WHO_Set2_Height_For_Age_Female.objects.all()),

    'length_for_age_male_sc' : serializers.serialize("json", WHO_Set2_Length_For_Age_Male.objects.all()),
    'length_for_age_female_sc' : serializers.serialize("json", WHO_Set2_Length_For_Age_Female.objects.all()),
  }
  return json.dumps(standard_curves)

def verify_registration(request):
  email = request.POST["email"]
  password = request.POST["password"]
  confirm_password = request.POST["confirm-password"]
  
  # TODO: Use a form validation library
  if (email == ''):
    return "You must enter a valid email"

  if (password == '' or confirm_password == ''):
    return "You must enter a password"

  if (password != confirm_password):
    return "Paswords do not match"

  # Otherwise all fields entered correctly, check database that user doesnt exist
  else:
    user = User.objects.create_user(username=email, email=email, password=password)
    user.save()
    post_save.connect(create_user, sender=User)

  # TODO: Constraint checking
  return None


# Logs user in and get their profile
def get_profile(request):
  email = request.POST["email"]
  password = request.POST["password"]

  # TODO: Use a form validation library
  if (email == ''):
    return "You must enter a valid email"

  if (password == ''):
    return "You must enter a password"

  else:
    user = authenticate(username=email, password=password)
    if user is not None:
      if user.is_active:
        login(request, user)
      else:
        return "Your account has been disabled"
    else:
      return "That user does not exist, please register."

  return None

def add_child(request):
  parent_id = request.user.id
  name = request.POST["name"]
  dob = request.POST["date-of-birth"]
  sex = request.POST["sex"]

  # TODO: Use a form validation library
  # TODO: Check valid inputs

  child = Child(name=name, date_of_birth=dob, sex=sex, parent_id=parent_id)
  child.save()
  
  return None

def get_children(request):
  # TODO: Change this
  parent_id = request.user.id
  children = Child.objects.filter(parent_id=parent_id).all()
  children_json = serializers.serialize("json", children)
  return children, children_json

def get_child_profile(request):
  parent_id = request.user.id
  child_id = request.POST["child_id"]
  child_profile_obj = Child.objects.filter(parent_id=parent_id, id=child_id).all()

  _dob = datetime.strptime(child_profile_obj[0].date_of_birth.strftime("%Y-%m-%d"), "%Y-%m-%d")

  relative_dob = relativedelta(todays_date(), _dob)
  
  formatted_dob = child_profile_obj[0].date_of_birth.strftime("%d%b%Y")

  child_profile = {
    'name' : child_profile_obj[0].name,
    'dob' : formatted_dob,
    'sex' : child_profile_obj[0].sex,
    'age' : str(relative_dob.years) + "y" + " " + str(relative_dob.months) + "m",
    'last_entry_date' : '',
    'last_weight' : None,
    'last_length' : None,
    'last_head_circumference' : None,
    'last_bmi' : None
  }

  log_entries = get_log_entries(child_id)
  
  last_entry_length = len(log_entries)
  if last_entry_length != 0:
    last_entry = log_entries[len(log_entries)-1]
    child_profile["last_entry_date"] = 'as of ' + last_entry.date_of_measurement.strftime("%d%b%Y")
    child_profile["last_weight"] = last_entry.weight
    child_profile["last_length"] = last_entry.length
    child_profile["last_head_circumference"] = last_entry.head_circumference
    child_profile["last_bmi"] = last_entry.bmi

  return child_profile


def enter_log(request):
  # TODO: Use a form validation library
  # TODO: Check valid inputs

  parent_id = request.user.id

  child_id = request.POST["child-id"]
  date_of_measurement = request.POST["date-of-measurement"]
  length = request.POST["length"]
  weight = request.POST["weight"]
  head_circumference = request.POST["head-circumference"]
  location = request.POST["location"]

  child_profile_obj = Child.objects.filter(parent_id=parent_id, id=child_id).all()

  _dob = datetime.strptime(child_profile_obj[0].date_of_birth.strftime("%Y-%m-%d"), "%Y-%m-%d")
  _dom = datetime.strptime(date_of_measurement, "%Y-%m-%d")

  delta = abs(_dob - _dom).days

  log_entry = Log_Entry(child_id=child_id, date_of_measurement=date_of_measurement, date_of_entry=todays_date(), length=length, weight=weight, bmi=10, age=delta)
  log_entry.save()
  return None

def get_log_entries(child_id):
  all_log_entries = Log_Entry.objects.filter(child_id=child_id).order_by('date_of_measurement').all()
  return all_log_entries

# Helper functions
def age_in_days(date_of_birth, date):
  #TOD0:
  return None

def age_in_months(date_of_birth, date):
  #TODO:
  return None

def todays_date():
  return datetime.strptime(date.today().strftime("%Y-%m-%d"), "%Y-%m-%d")