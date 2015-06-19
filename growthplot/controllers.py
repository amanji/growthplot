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
from django.db import IntegrityError
import time
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import json

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
    try:
      user = User.objects.create_user(username=email, email=email, password=password)
      user.save()
      return None
    except IntegrityError as e:
      print e.__cause__
      return 'That user already exists, please <a href="/login">login</a> or click <a href="/forgotpassword">Forgot Password</a> to retrieve your credentials.'

# Logs user in and get their profile
def get_profile(request):
  email = request.POST["email"]
  password = request.POST["password"]

  # TODO: Use a form validation library
  if (email == ''):
    return "You must enter a valid email"

  if (password == ''):
    return "You must enter a password"

  user = authenticate(username=email, password=password)
  if user is not None:
    # if user.is_active:
    login(request, user)
    return None, True
    # else:
    #   return "Your account has been disabled", True
  else:
    if(User.objects.filter(username=email).count()):
      return "Wrong Password!", None
    return None, None

def chart(request):
  #TODO:
  chart_type = request.POST["chart"] + "-" + request.POST["age"];
  chart = request.POST["chart"]
  age_category = request.POST["age"]
  child_id = request.POST["child_id"]
  parent_id = request.user.id

  chart_types = {
  "weight-for-age-female-" : get_weight_for_age(child_id, parent_id, age_category, "F"),
  "weight-for-age-male-" : get_weight_for_age(child_id, parent_id, age_category, "M"),
  "height-for-age-female-" : get_height_for_age(child_id, parent_id, age_category, "F"),
  "height-for-age-male-" : get_height_for_age(child_id, parent_id, age_category, "M"),
  "bmi-female-" : get_bmi(child_id, parent_id, age_category, "F"),
  "bmi-male-" : get_bmi(child_id, parent_id, age_category, "M"),
  "weight-for-age-female-birth" : get_weight_for_age(child_id, parent_id, age_category, "F"),
  "weight-for-age-male-birth" : get_weight_for_age(child_id, parent_id, age_category, "M"),
  "length-for-age-female-birth" : get_height_for_age(child_id, parent_id, age_category, "F"),
  "length-for-age-male-birth" : get_height_for_age(child_id, parent_id, age_category, "M"),
  "weight-for-length-female-birth" : get_weight_for_length(child_id, parent_id, age_category, "F"),
  "weight-for-length-male-birth" : get_weight_for_length(child_id, parent_id, age_category, "M"),
  "head-circumference-female-birth" : get_head_circumference(child_id, parent_id, age_category, "F"),
  "head-circumference-male-birth" : get_head_circumference(child_id, parent_id, age_category, "M"),
  }
  
  # Get relevant chart
  chart_data = chart_types[chart_type]

  return chart_data

def get_head_circumference(child_id, parent_id, age_category, sex):
  log_entries = get_log_entries(child_id)

  if sex == "F":
    standard_curve = WHO_Set2_Head_Circumference_Female.objects.all()
  else:
    standard_curve = WHO_Set2_Head_Circumference_Male.objects.all()

  chart_data = {
    'xAxis' : "Age (months)",
    'yAxis' : "Head Circumference (cm)",
    'data' : [],
    'standard_curve' : [],
    'title' : "Head Circumference"
  }

  for log_entry in log_entries:
    if log_entry.birth:
      age_months = round((log_entry.age/365.2425)*12,1)
      chart_data['data'].append({"Head Circumference (cm)" : log_entry.head_circumference, "Age (months)" : age_months})

  for sc_entry in standard_curve:
    chart_data['standard_curve'].append({"p3" : sc_entry.p3, "p10" : sc_entry.p10, "p25" : sc_entry.p25, "p50" : sc_entry.p50, "p75" : sc_entry.p75, "p90" : sc_entry.p90, "p97" : sc_entry.p97, "Age (months)" : sc_entry.month, 'label' : False})
  
  return json.dumps(chart_data)


def get_weight_for_length(child_id, parent_id, age_category, sex):
  log_entries = get_log_entries(child_id)

  if sex == "F":
    standard_curve = WHO_Set2_Weight_For_Length_Female.objects.all()
  else:
    standard_curve = WHO_Set2_Weight_For_Length_Male.objects.all()

  chart_data = {
    'xAxis' : "Length (cm)",
    'yAxis' : "Weight (kg)",
    'data' : [],
    'standard_curve' : [],
    'title' : "Weight for Length"
  }

  for log_entry in log_entries:
    if log_entry.birth:
      chart_data['data'].append({"Weight (kg)" : log_entry.weight, "Length (cm)" : log_entry.length})

  for sc_entry in standard_curve:
    chart_data['standard_curve'].append({"p3" : sc_entry.p3, "p10" : sc_entry.p10, "p25" : sc_entry.p25, "p50" : sc_entry.p50, "p75" : sc_entry.p75, "p90" : sc_entry.p90, "p97" : sc_entry.p97, "Length (cm)" : sc_entry.length, 'label' : False})
  
  return json.dumps(chart_data)


def get_weight_for_age(child_id, parent_id, age_category, sex):
  # Set yMin and yMax
  log_entries = get_log_entries(child_id)

  if sex == "F":
    standard_curve = WHO_Set2_Weight_For_Age_Female.objects.all()
  else:
    standard_curve = WHO_Set2_Weight_For_Age_Male.objects.all()

  if age_category == 'birth':

    chart_data = {
      'xAxis' : "Age (months)",
      'yAxis' : "Weight (kg)",
      'data' : [],
      'standard_curve' : [],
      'title' : "Weight for Age"
    }

    for log_entry in log_entries:
      if log_entry.birth:
        age_months = round((log_entry.age/365.2425)*12,1)
        chart_data['data'].append({"Weight (kg)" : log_entry.weight, "Age (months)" : age_months})

    for sc_entry in standard_curve:
      if sc_entry.month <= 24:
        chart_data['standard_curve'].append({"p3" : sc_entry.p3, "p10" : sc_entry.p10, "p25" : sc_entry.p25, "p50" : sc_entry.p50, "p75" : sc_entry.p75, "p90" : sc_entry.p90, "p97" : sc_entry.p97, "Age (months)" : sc_entry.month, 'label' : False})
    
  else:

    chart_data = {
      'xAxis' : "Age (years)",
      'yAxis' : "Weight (kg)",
      'data' : [],
      'standard_curve' : [],
      'title' : "Weight for Age"
    }

    for log_entry in log_entries:
      age_years = round((float(log_entry.age)/365.2425), 1)
      chart_data['data'].append({"Weight (kg)" : log_entry.weight, "Age (years)" : age_years})

    for sc_entry in standard_curve:
      age_years = round((float(sc_entry.month)/12), 1)
      chart_data['standard_curve'].append({"p3" : sc_entry.p3, "p10" : sc_entry.p10, "p25" : sc_entry.p25, "p50" : sc_entry.p50, "p75" : sc_entry.p75, "p90" : sc_entry.p90, "p97" : sc_entry.p97, "Age (years)" : age_years, 'label' : False})

  return json.dumps(chart_data)

def get_height_for_age(child_id, parent_id, age_category, sex):
  # Set yMin and yMax
  log_entries = get_log_entries(child_id)

  if age_category == 'birth':

    if sex == "F":
      standard_curve = WHO_Set2_Length_For_Age_Female.objects.all()
    else:
      standard_curve = WHO_Set2_Length_For_Age_Male.objects.all()


    chart_data = {
      'xAxis' : "Age (months)",
      'yAxis' : "Length (cm)",
      'data' : [],
      'standard_curve' : [],
      'title' : "Length for Age"
    }

    for log_entry in log_entries:
      if log_entry.birth:
        age_months = round((log_entry.age/365.2425)*12,1)
        chart_data['data'].append({"Length (cm)" : log_entry.length, "Age (months)" : age_months})

    for sc_entry in standard_curve:
      if sc_entry.month <= 24:
        chart_data['standard_curve'].append({"p3" : sc_entry.p3, "p10" : sc_entry.p10, "p25" : sc_entry.p25, "p50" : sc_entry.p50, "p75" : sc_entry.p75, "p90" : sc_entry.p90, "p97" : sc_entry.p97, "Age (months)" : sc_entry.month, 'label' : False})
    
  else:

    if sex == "F":
      standard_curve = WHO_Set2_Height_For_Age_Female.objects.all()
    else:
      standard_curve = WHO_Set2_Height_For_Age_Male.objects.all()


    chart_data = {
      'xAxis' : "Age (years)",
      'yAxis' : "Height (cm)",
      'data' : [],
      'standard_curve' : [],
      'title' : "Height for Age"
    }

    for log_entry in log_entries:
      age_years = round((float(log_entry.age)/365.2425), 1)
      chart_data['data'].append({ "Height (cm)" : log_entry.length, "Age (years)" : age_years})

    for sc_entry in standard_curve:
      age_years = round((float(sc_entry.month)/12), 1)
      chart_data['standard_curve'].append({"p3" : sc_entry.p3, "p10" : sc_entry.p10, "p25" : sc_entry.p25, "p50" : sc_entry.p50, "p75" : sc_entry.p75, "p90" : sc_entry.p90, "p97" : sc_entry.p97, "Age (years)" : age_years, 'label' : False})

  return json.dumps(chart_data)


def get_bmi(child_id, parent_id, age_category, sex):
  # Set yMin and yMax
  log_entries = get_log_entries(child_id)

  if sex == "F":
    standard_curve = WHO_Set2_BMI_Female.objects.all()
  else:
    standard_curve = WHO_Set2_BMI_Male.objects.all()

  chart_data = {
  'xAxis' : "Age (years)",
  'yAxis' : "BMI (kg/m^2)",
  'data' : [],
  'standard_curve' : [],
  'title' : "BMI for Age"
  }

  for log_entry in log_entries:
    age_years = round((float(log_entry.age)/365.2425), 1)
    chart_data['data'].append({"BMI (kg/m^2)" : log_entry.weight, "Age (years)" : age_years})

  for sc_entry in standard_curve:
    age_years = round((float(sc_entry.month)/12), 1)
    chart_data['standard_curve'].append({"p3" : sc_entry.p3, "p10" : sc_entry.p10, "p25" : sc_entry.p25, "p50" : sc_entry.p50, "p75" : sc_entry.p75, "p85" : sc_entry.p85, "p97" : sc_entry.p97, "Age (years)" : age_years})
  
  return json.dumps(chart_data)

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

  less_than_2 = (relative_dob.years < 2)

  child_profile = {
    'name' : child_profile_obj[0].name,
    'dob' : formatted_dob,
    'sex' : child_profile_obj[0].sex,
    'age' : str(relative_dob.years) + "y" + " " + str(relative_dob.months) + "m",
    'less_than_2' : less_than_2,
    'last_entry_date' : '',
    'last_weight' : None,
    'last_length' : None,
    'last_head_circumference' : None,
    'last_bmi' : None
  }

  log_entries = get_log_entries(child_id, True)
  
  last_entry_length = len(log_entries)
  if last_entry_length != 0:
    last_entry = log_entries[0]
    child_profile["last_entry_date"] = 'as of ' + last_entry.date_of_measurement.strftime("%d%b%Y")
    child_profile["last_weight"] = last_entry.weight
    child_profile["last_length"] = last_entry.length
    child_profile["last_head_circumference"] = last_entry.head_circumference
    child_profile["last_bmi"] = last_entry.bmi

  return child_profile, log_entries

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

  age_days = age_in_days(_dob, _dom)
  age_years_boolean = (relative_age_in_years(_dob, _dom) < 2)

  log_entry = Log_Entry(child_id=child_id, date_of_measurement=date_of_measurement, date_of_entry=todays_date(), length=round(float(length), 1), weight=round(float(weight),1), bmi=round(bmi(weight, length),1), head_circumference=round(float(head_circumference),1), age=age_days, birth=age_years_boolean)
  log_entry.save()
  return None

def get_log_entries(child_id, desceding_order=None):
  if desceding_order:
    all_log_entries = Log_Entry.objects.filter(child_id=child_id).order_by('-date_of_measurement').all()
  else:
    all_log_entries = Log_Entry.objects.filter(child_id=child_id).order_by('date_of_measurement').all()
  return all_log_entries

# Helper functions
##################

def todays_date():
  return datetime.strptime(date.today().strftime("%Y-%m-%d"), "%Y-%m-%d")

def age_in_days(date_of_birth, date):
  return abs(date_of_birth - date).days

def age_in_months(date_of_birth, date):
  #TODO:
  return None

def relative_age_in_years(date_of_birth, date):
  return relativedelta(date, date_of_birth).years

def bmi(weight, length):
  return (float(weight)/(float(length)/100)**2)