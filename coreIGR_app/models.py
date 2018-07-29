from django.db import models

# Create your models here.

# class TransactionType(models.Model):
#     t_type = models.CharField(unique = True, max_length = 50)

class AssignedTin(models.Model):
	TIN_FOR = (	("Individual", "Individual"),	("Company", "Company")	)
	registration_date = models.DateField(auto_now_add=True)
	tin = models.CharField(max_length = 10)
	
	tin_for = models.CharField(max_length = 15, choices = TIN_FOR)

class InstitutionCategory(models.Model):
    category_name = models.CharField(unique = True, max_length = 50, null = False)

class InstitutionType(models.Model):
    type_name = models.CharField(unique = True, max_length = 50, null = False)


class Office(models.Model):
  office_name = models.CharField(max_length = 255, unique = True)
  is_active = models.BooleanField(default = True)

 

 

class User(models.Model):
	"""docstring for ClassName"""
	ACCSESS_LEVEL = (

        ("Super Administrator", "Super Administrator"),
        ("TIN User", "TIN User"),
        ("MLA User", "MLA User"),
        ("MLA Administrator", "MLA Administrator"),
        ("PAYEE User", "PAYEE User"),
        ("DA User", "DA User"),
        ("Store User", "Store User")
		)
	registration_date = models.DateField(auto_now_add=True)
	full_name = models.CharField(max_length = 50, null = False)
	department = models.CharField(max_length = 250, null = False)
	office = models.ForeignKey( Office, on_delete=models.CASCADE)
	user_name = models.CharField(max_length = 50, unique = True, null = False)
	password = models.CharField(max_length = 50,default = "password")
	access_level =  models.CharField(max_length = 50, choices = ACCSESS_LEVEL)
	is_active = models.BooleanField(default = True)
	is_password_changed =  models.BooleanField(default = False)

	# add some contratits here


    
class Charge(models.Model):
	OPTIONS = (
		("New", "New"),
		("Renew", "Renew")
		)
	options = models.CharField(max_length = 10, null = False, choices = OPTIONS )
	vehicle_type = models.CharField(max_length = 150, null = False)
	particulars	=  models.CharField(max_length = 150)
	amount = models.FloatField(null = True)

class ChargesOthers(models.Model):
    particulars	=  models.CharField(max_length = 150)
    amount = models.FloatField(null = False)

class LearnersPermit(models.Model):

	GENDER = (
		("M", "Male"),
		("F", "Female")
		)
	is_active = models.BooleanField(default = True)
	transaction_code = models.CharField(max_length = 15, null = False)
	tin =  models.ForeignKey(AssignedTin, null = False, on_delete = models.CASCADE)
	name = models.CharField(max_length = 50, null = False)
	gender = models.CharField(max_length = 10, choices = GENDER, null = False) 
	# make this come from choices
	address = models.CharField(max_length = 250, null = False)
	phone = models.CharField(max_length = 15, null = False)
	issue_date = models.DateField()
	expiration_date = models.DateField()
	particulars = models.CharField(max_length = 150)
	amount = models.FloatField(null = False)
	staff = models.ForeignKey( User, on_delete=models.CASCADE, null = False)
	office = models.ForeignKey( Office, on_delete=models.CASCADE)

class LocalGovArea(models.Model):
      local_government_name = models.CharField(unique = True, max_length = 50, null = False)
      local_government_code = models.CharField(unique = True, max_length = 2, null = False)



class Vehicle(models.Model):
	"""docstring for ClassName"""
	old_owners_tin =  models.CharField(max_length = 10 )
	current_owner_tin = models.ForeignKey(AssignedTin, null = False,on_delete=models.CASCADE)
	registration_date = models.DateField(auto_now_add=True)
	chassis_number = models.CharField(unique = True, max_length = 50, null = False)
	vehicle_model = models.CharField(max_length = 100, null = False)
	number_plate = models.CharField(unique = True, max_length = 8, null = False)
	vehicle_category = models.CharField(max_length = 50, null = False)
	gross_weight = models.IntegerField(null = False)
	net_weight = models.IntegerField()
	no_of_passengers = models.IntegerField()
	colour = models.CharField(max_length = 30)
	weight = models.IntegerField()
	engine_size = models.CharField(max_length = 15)
	cost_price = models.CharField(max_length = 50, null = True)
	theft_status = models.BooleanField(default = False)
	staff = models.ForeignKey( User, on_delete=models.CASCADE, null = False)
	office = models.ForeignKey( Office, on_delete=models.CASCADE, null = False)

	# PK at offices

 

class NumberPlate(models.Model):
	"""docstring for NumberPlate"""
	registration_date = models.DateField(auto_now_add=True)
	local_government = models.CharField(max_length = 50, null = False)
	number_plate  = models.CharField(primary_key =True, max_length = 8)
	staff = models.ForeignKey( User, on_delete=models.CASCADE, null = False)
	is_issued = models.BooleanField(default = False)

class AssignedNumberPlate(models.Model):
	"""docstring for NumberPlate"""
	registration_date = models.DateField(auto_now_add=True)
	office =  models.ForeignKey( Office, on_delete=models.CASCADE, null = False)
	number_plate  = models.ForeignKey(NumberPlate, on_delete=models.CASCADE, null = False)
	is_issued = models.BooleanField(default = False)
		

class StateCode(models.Model):
	"""docstring for StatusCode"""
	state_code = models.CharField(max_length = 2, null = False)
	# state_name = models.CharField(max_length = 30, null = False)




class Revalidation(models.Model):
	"""docstring for revalidation"""
	transaction_date = models.DateField(auto_now_add=True)
	tin = models.ForeignKey(AssignedTin, on_delete=models.CASCADE, null = False)
	name = models.CharField(max_length = 50, null = False)
	old_plate_number = models.CharField(max_length = 8, null = False)
	new_plate_number = models.CharField(max_length = 8, null = False)


# correct this
class Individual(models.Model):

	GENDER = (
		("Male", "Male"),
		("Female", "Female")
		)
	MARITAL_STATUS = (
		("Married", "Married"),
		("Single", "Single"),
		("Divorced", "Divorced"),
		("Others", "Others")
		)
	registration_date = models.DateField(auto_now_add=True)
	tin = models.ForeignKey(AssignedTin, on_delete=models.CASCADE)
	name = models.CharField(max_length = 50 ,null = False)
	gender = models.CharField(max_length = 10, choices = GENDER)
	date_of_birth = models.CharField(max_length = 20)
	marital_status = models.CharField(max_length = 15, choices = MARITAL_STATUS)
	state = models.CharField(max_length = 50)
	address = models.CharField(max_length = 250, null = False)
	phone = models.CharField(max_length = 15)
	email = models.CharField(max_length = 100, null = False)
	occupation = models.CharField(max_length = 50 ,null = False)
	employment_status = models.CharField(max_length = 15 ,null = False)
	work_place = models.CharField(max_length = 250)
	passport_id = models.CharField(max_length = 25)
	staff = models.ForeignKey(User, on_delete = models.CASCADE)
	office = models.ForeignKey(Office, on_delete=models.CASCADE, null = False)

#  make gender table


class TransactionAssessment (models.Model):
  is_expired  = models.BooleanField(default = False, null = False )
  transaction_code = models.CharField( max_length = 15, null = False )  
  tin = models.ForeignKey(AssignedTin, null = False, on_delete = models.CASCADE)
  chassis_number = models.CharField(max_length = 17, null = False)
  particulars = models.CharField(max_length = 250, null = False)
  amount = models.FloatField(null = False)
  transaction_date =  models.DateField(auto_now_add=True)
  issue_date = models.DateField(auto_now_add=True)
  expiration_date = models.DateField( null = True)
  transaction_type = models.CharField(max_length = 50)
  payment_status = models.CharField(max_length = 10)
  status = models.BooleanField(default = True)
  transaction_staff = models.ForeignKey( User, on_delete=models.CASCADE, null = False)
  transaction_office = models.ForeignKey( Office, on_delete=models.CASCADE, null = False)


class Company(models.Model):

  registration_date = models.DateField(auto_now_add=True)
  local_government = models.CharField(max_length = 50)
  ward = models.CharField(max_length = 50)
  bussiness_area = models.CharField(max_length = 5)
  institution = models.CharField(max_length = 50)
  institution_type =  models.ForeignKey(InstitutionType, on_delete=models.CASCADE)
  institution_category =  models.ForeignKey(InstitutionCategory, on_delete=models.CASCADE)
  bussiness_status = models.CharField(max_length = 50)
  bussiness_class = models.CharField(max_length = 50)
  registration_number = models.CharField(max_length = 20)
  bussiness_ownership_type = models.CharField(max_length = 50)
  tin = models.ForeignKey(AssignedTin, on_delete=models.CASCADE)
  jtb_tin = models.CharField(max_length = 10)
  bussiness_name = models.CharField(max_length = 250)
  bussiness_owner = models.CharField(max_length = 250)
  bussiness_address = models.CharField(max_length = 250)
  phone_number = models.CharField(max_length = 15)
  email = models.CharField(max_length = 100)
  bussiness_size = models.CharField(max_length = 50)
  longtitude = models.CharField(max_length = 10)    
  latitude = models.CharField(max_length = 10)
  enumerator = models.CharField(max_length = 50)
  supervisor = models.CharField(max_length = 50)
  coordinator = models.CharField(max_length = 50)
  staff =models.ForeignKey( User, on_delete=models.CASCADE, null = False)
  office =  models.ForeignKey( Office, on_delete=models.CASCADE)
  # password = models.CharField(max_length = 50, default = "admin")


class PayeeTaxpayer(models.Model):
  staff_id =  models.ForeignKey(User, null = False, on_delete=models.CASCADE)
  staff_name = models.CharField(max_length = 50)
  company_tin =  models.ForeignKey(AssignedTin, null = False, on_delete=models.CASCADE)
  company_name = models.CharField(max_length = 250)
  total_gross_income = models.FloatField()
  pension = models.BooleanField(default = False)
  NHIS = models.FloatField()
  NHF = models.BooleanField()
  life_assurance  = models.FloatField()


class MDAList(models.Model):
  mda_name = models.CharField(max_length = 250, unique = True)




class MDA(models.Model):
  admin_code = models.CharField(max_length = 15)
  mda_name = models.CharField(max_length = 250)
  eco_code = models.CharField(max_length = 15)
  group_title = models.CharField(max_length = 250)
  ipsas_code = models.CharField(max_length = 15)
  ipsas_title = models.CharField(max_length = 250)
  aprvd_18 = models.FloatField(max_length = 50)

class RevenueItem(models.Model):
  admin_code = models.CharField(max_length = 15)
  mda_name = models.CharField(max_length = 250)
  eco_code = models.CharField(max_length = 15)
  group_title = models.CharField(max_length = 250)
  ipsas_code = models.CharField(max_length = 15)
  ipsas_title = models.CharField(max_length = 250)
  aprvd_18 = models.FloatField(max_length = 50)

class MDAEbill(models.Model):
  transaction_date =  models.DateField()
  reference_number = models.CharField(max_length = 20)
  tin = models.ForeignKey(AssignedTin, null = False, on_delete=models.CASCADE)
  name = models.CharField(max_length = 250)
  mda = models.ForeignKey(MDA, null = False, on_delete=models.CASCADE)  
  revenue_item = models.CharField(max_length = 250)
  period = models.CharField(max_length = 250)
  amount = models.FloatField()
  is_paid = models.BooleanField(default = False)

#  add not null constrait