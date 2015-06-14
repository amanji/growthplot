from django.db import models

class Parent(models.Model):
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)

GENDER_CHOICES = (
  ('M', 'Male'),
  ('F', 'Female'),
  )

ACTIVE_CHOICES = (
  ('A', 'Active'),
  ('I', 'Inactive'),
  )

class Child(models.Model):
  parent_id = models.ForeignKey(Parent, null=False)
  date_of_birth = models.DateTimeField('date of birth')
  sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
  active_flag = models.CharField(max_length=1, choices=ACTIVE_CHOICES)

class Log_Entry(models.Model):
  date_of_entry = models.DateTimeField('date of log entry')
  date_of_measurement = models.DateTimeField('date measurement was taken')
  child_id = models.ForeignKey(Child, null=False)
  height = models.FloatField()
  weight = models.FloatField()
  head_circumference = models.FloatField()
  bmi = models.FloatField()
  age = models.IntegerField()


# The foloowing tables are for ages 0-2 years
#############################################

# M
class WHO_Set2_Weight_For_Length_Male(models.Model):
  length = models.FloatField('length in centimeters')
  L = models.FloatField()
  M = models.FloatField()
  S = models.FloatField()
  p3 = models.FloatField('3rd percentile')
  p10 = models.FloatField('10th percentile')
  p25 = models.FloatField('25th percentile')
  p50 = models.FloatField('50th percentile')
  p75 = models.FloatField('75th percentile')
  p90 = models.FloatField('90th percentile')
  p97 = models.FloatField('97th percentile')

# F
class WHO_Set2_Weight_For_Length_Female(models.Model):
  length = models.FloatField('length in centimeters')
  L = models.FloatField()
  M = models.FloatField()
  S = models.FloatField()
  p3 = models.FloatField('3rd percentile')
  p10 = models.FloatField('10th percentile')
  p25 = models.FloatField('25th percentile')
  p50 = models.FloatField('50th percentile')
  p75 = models.FloatField('75th percentile')
  p90 = models.FloatField('90th percentile')
  p97 = models.FloatField('97th percentile')

# M
class WHO_Set2_Head_Circumference_Male(models.Model):
  month = models.FloatField('length in centimeters')
  L = models.FloatField()
  M = models.FloatField()
  S = models.FloatField()
  p3 = models.FloatField('3rd percentile')
  p10 = models.FloatField('10th percentile')
  p25 = models.FloatField('25th percentile')
  p50 = models.FloatField('50th percentile')
  p75 = models.FloatField('75th percentile')
  p90 = models.FloatField('90th percentile')
  p97 = models.FloatField('97th percentile')

# F
class WHO_Set2_Head_Circumference_Female(models.Model):
  month = models.FloatField('length in centimeters')
  L = models.FloatField()
  M = models.FloatField()
  S = models.FloatField()
  p3 = models.FloatField('3rd percentile')
  p10 = models.FloatField('10th percentile')
  p25 = models.FloatField('25th percentile')
  p50 = models.FloatField('50th percentile')
  p75 = models.FloatField('75th percentile')
  p90 = models.FloatField('90th percentile')
  p97 = models.FloatField('97th percentile')

# M
class WHO_Set2_Length_For_Age_Male(models.Model):
  month = models.FloatField('length in centimeters')
  L = models.FloatField()
  M = models.FloatField()
  S = models.FloatField()
  p3 = models.FloatField('3rd percentile')
  p10 = models.FloatField('10th percentile')
  p25 = models.FloatField('25th percentile')
  p50 = models.FloatField('50th percentile')
  p75 = models.FloatField('75th percentile')
  p90 = models.FloatField('90th percentile')
  p97 = models.FloatField('97th percentile')

# F
class WHO_Set2_Length_For_Age_Female(models.Model):
  month = models.FloatField('length in centimeters')
  L = models.FloatField()
  M = models.FloatField()
  S = models.FloatField()
  p3 = models.FloatField('3rd percentile')
  p10 = models.FloatField('10th percentile')
  p25 = models.FloatField('25th percentile')
  p50 = models.FloatField('50th percentile')
  p75 = models.FloatField('75th percentile')
  p90 = models.FloatField('90th percentile')
  p97 = models.FloatField('97th percentile')

# The following tables are for ages from 0-19
#############################################

# M
class WHO_Set2_Weight_For_Age_Male(models.Model):
  month = models.FloatField('length in centimeters')
  L = models.FloatField()
  M = models.FloatField()
  S = models.FloatField()
  p3 = models.FloatField('3rd percentile')
  p10 = models.FloatField('10th percentile')
  p25 = models.FloatField('25th percentile')
  p50 = models.FloatField('50th percentile')
  p75 = models.FloatField('75th percentile')
  p90 = models.FloatField('90th percentile')
  p97 = models.FloatField('97th percentile')

# F
class WHO_Set2_Weight_For_Age_Female(models.Model):
  month = models.FloatField('length in centimeters')
  L = models.FloatField()
  M = models.FloatField()
  S = models.FloatField()
  p3 = models.FloatField('3rd percentile')
  p10 = models.FloatField('10th percentile')
  p25 = models.FloatField('25th percentile')
  p50 = models.FloatField('50th percentile')
  p75 = models.FloatField('75th percentile')
  p90 = models.FloatField('90th percentile')
  p97 = models.FloatField('97th percentile')

# The following tables are for ages 2-19
########################################

# M
class WHO_Set2_Height_For_Age_Male(models.Model):
  month = models.FloatField('length in centimeters')
  L = models.FloatField()
  M = models.FloatField()
  S = models.FloatField()
  p3 = models.FloatField('3rd percentile')
  p10 = models.FloatField('10th percentile')
  p25 = models.FloatField('25th percentile')
  p50 = models.FloatField('50th percentile')
  p75 = models.FloatField('75th percentile')
  p90 = models.FloatField('90th percentile')
  p97 = models.FloatField('97th percentile')

# F
class WHO_Set2_Height_For_Age_Female(models.Model):
  month = models.FloatField('length in centimeters')
  L = models.FloatField()
  M = models.FloatField()
  S = models.FloatField()
  p3 = models.FloatField('3rd percentile')
  p10 = models.FloatField('10th percentile')
  p25 = models.FloatField('25th percentile')
  p50 = models.FloatField('50th percentile')
  p75 = models.FloatField('75th percentile')
  p90 = models.FloatField('90th percentile')
  p97 = models.FloatField('97th percentile')

# M
class WHO_Set2_BMI_Male(models.Model):
  month = models.FloatField('length in centimeters')
  L = models.FloatField()
  M = models.FloatField()
  S = models.FloatField()
  p3 = models.FloatField('3rd percentile')
  p10 = models.FloatField('10th percentile')
  p25 = models.FloatField('25th percentile')
  p50 = models.FloatField('50th percentile')
  p75 = models.FloatField('75th percentile')
  p85 = models.FloatField('90th percentile')
  p97 = models.FloatField('97th percentile')

# F
class WHO_Set2_BMI_Female(models.Model):
  month = models.FloatField('length in centimeters')
  L = models.FloatField()
  M = models.FloatField()
  S = models.FloatField()
  p3 = models.FloatField('3rd percentile')
  p10 = models.FloatField('10th percentile')
  p25 = models.FloatField('25th percentile')
  p50 = models.FloatField('50th percentile')
  p75 = models.FloatField('75th percentile')
  p85 = models.FloatField('90th percentile')
  p97 = models.FloatField('97th percentile')