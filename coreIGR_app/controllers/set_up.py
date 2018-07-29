from django.shortcuts import render
from django.db import IntegrityError
from django.contrib import messages
from coreIGR_app.models import User, Office, LocalGovArea, StateCode, Charge, InstitutionCategory, InstitutionType
from coreIGR_app.controllers.dashboard import dashboard

from coreIGR_app.forms import LoginForm, UserForm, LocalGovAreaForm, OfficeForm, StateCodeForm, ChargeForm, InstitutionCategoryForm, InstitutionTypeForm

from django.http import HttpResponseRedirect


def user_login(req):
	if req.method == "GET" and   ('user_id' not in req.session):
		# load login form 
		return render(req, 'login.html')

	elif ('user_id' in req.session) and ('access_level' in req.session):
		# user is already logged in
		dashboard(req)
		return render(req, 'dashboard.html')
		
		
	elif req.method == "POST" and req.POST:
		# user is logining in

		form = LoginForm(req.POST)
		if form.is_valid():			 
			
			# field not validated
			user_name = req.POST.get("user_name")
			paswd = form.cleaned_data.get('password')

			try:				 

				user = User.objects.get(user_name = user_name, password = paswd)

				if user.is_active:
					if not user.is_password_changed:						
						
						req.session['office_id'] = user.office.id
						req.session['access_level'] = user.access_level
						req.session['name'] = user.full_name
						req.session['user_id'] = user.id

						dashboard(req)
						return render(req, 'dashboard.html')

					else:
						req.session['temp_user_id'] = user.id
						req.session['temp_user_name'] = user.user_name
						messages.info(req, "Please change your password to continue")
						return render(req, 'dashboard.html')
				else:
					messages.info(req, "This account is not active")
					return render(req, 'login.html')					
			 					
			except User.DoesNotExist:
				# user does not exist
				messages.info(req, "Password or user name is wrong")
				return render(req, 'login.html')						
		else:
			
			messages.warning(req, "Please input correct data in fields")
			return render(req, 'login.html')
	else:
		return HttpResponseRedirect('/login/')
		



def add_new_user(req):

	form  = UserForm(req.POST)
	if form.is_valid():

		try:
			user_name = req.POST.get("user_name")
			user = form.save(commit = False)
			office_id = req.POST.get("office_id")

			office = Office.objects.get(id = office_id)
			 
			user.office =office
			user.user_name = user_name
			user.save()


			 
			messages.success(req, "user created", extra_tags = "record_created") 
			return HttpResponseRedirect('/set-up/add-user/')

		except Office.DoesNotExist:
			return HttpResponseRedirect('/login/')

		except Exception as e:			 
			messages.info(req, "uncaught Exception")
			return HttpResponseRedirect('/set-up/add-user/')
			
			
	else:
		if form['user_name'].errors: 
			messages.success(req, "uname taken")
			return HttpResponseRedirect('/set-up/add-user/')
			
	 
def add_new_office(req):
	
	form = OfficeForm(req.POST)

	if form.is_valid():
		

		try:
			office_name = form.cleaned_data.get("office_name")
			office_obj, created =  Office.objects.get_or_create(office_name = office_name)

			if created:
				 
				messages.success(req, "Office Created", extra_tags = "office_added")
				return HttpResponseRedirect('/set-up/add-office/')
			else:
				 
				messages.success(req, "Office already exist", extra_tags ="office_already_added")
				return HttpResponseRedirect('/set-up/add-office/')

		except Exception as e:
			print(e)
			 
			messages.info(req, "uncaught Exception")
			return HttpResponseRedirect('/set-up/add-office/')
	else:
		messages.success(req, "Invalid Data", extra_tags = "invalid_data")
		return HttpResponseRedirect('/set-up/add-office/')

	
def add_new_lga(req):

	form = LocalGovAreaForm(req.POST)

	if form.is_valid():
	
		try:
			lga_name = form.cleaned_data.get("local_government_name")
			lga_code = form.cleaned_data.get("local_government_code")
			lga_obj, created =  LocalGovArea.objects.get_or_create(local_government_name = lga_name, local_government_code = lga_code)

			if created:		

				messages.success(req, "LGA Created", extra_tags = "record_created")
				return HttpResponseRedirect('/set-up/add-lga/')

			else:				 
				messages.success(req, "LGA already exist")
				return HttpResponseRedirect('/set-up/add-lga/')

		except Exception as e:			 
			messages.info(req, "uncaught Exception")
			return HttpResponseRedirect('/set-up/add-lga/')		
		
	else:
		messages.info(req, "invalid form fields")
		return HttpResponseRedirect('/set-up/add-lga/')



def add_new_state_code(req):
	form = StateCodeForm(req.POST)

	if form.is_valid():
	
		try:
			
			state_code = form.cleaned_data.get("state_code")

			if (len(state_code) == 2):

				try:
					state_code_obj = StateCode.objects.get(id = 1)
					state_code_obj.state_code = state_code	
					state_code_obj.save()			
					 
					return HttpResponseRedirect('/set-up/lgas/')

				except StateCode.DoesNotExist:
					StateCode.objects.create(state_code = state_code)
					return HttpResponseRedirect('/set-up/lgas/')
					
			else:
				messages.success(req, "invalid State code ")
				return HttpResponseRedirect('/set-up/lgas/')
		 

		except Exception as e:
			print(e)
			
			messages.info(req, "uncaught Exception")
			return HttpResponseRedirect('/set-up/lgas/')		
		
	else:
		messages.info(req, "invalid form fields")
		return HttpResponseRedirect('/set-up/lgas/')



def add_new_charge(req):

	form = ChargeForm(req.POST)

	if form.is_valid():
	 

		try:
			change_type = form.cleaned_data.get("options")
			vehicle_type = form.cleaned_data.get("vehicle_type")
			particulars = form.cleaned_data.get("particulars")
			amount = form.cleaned_data.get("amount")

			try:
				Charge.objects.get(options = change_type, vehicle_type = vehicle_type, particulars  = particulars)
				messages.info(req, "change exist")
				return HttpResponseRedirect('/set-up/add-charge/')

			except Charge.DoesNotExist:
				try:
					Charge.objects.create(options = change_type, vehicle_type = vehicle_type, particulars = particulars, amount = amount)
					messages.success(req, "LGA Created", extra_tags = "record_created")
					return HttpResponseRedirect('/set-up/add-charge/')
				except Exception as e:		
					return HttpResponseRedirect('/set-up/add-charge/')

		 

		except Exception as e:	
			print(e)		 
			messages.info(req, "uncaught Exception")
			return HttpResponseRedirect('/set-up/add-charge/')		
		
	else:
		print(form.errors)
		messages.info(req, "invalid form fields")
		return HttpResponseRedirect('/set-up/add-charge/')






def add_new_institution_category(req):

	form = InstitutionCategoryForm(req.POST)

	if form.is_valid():
		category_name = form.cleaned_data.get("category_name")		 

		try:
			InstitutionCategory.objects.create(category_name = category_name)
			messages.info(req, "Institution Category created", extra_tags = "record_created")
			return HttpResponseRedirect('/set-up/add-institution-category/')

		
		except Exception as e:	
			print(e)		 
			messages.info(req, "uncaught Exception")
			return HttpResponseRedirect('/set-up/add-institution-category/')		
		
	else:
		print(form.errors)
		messages.info(req, "invalid form fields")
		return HttpResponseRedirect('/set-up/add-institution-category/')

def add_new_institution_type(req):

	form = InstitutionTypeForm(req.POST)

	if form.is_valid():
		type_name = form.cleaned_data.get("type_name")		 

		try:
			InstitutionType.objects.create(type_name = type_name)
			messages.info(req, "Institution Type created", extra_tags = "record_created")
			return HttpResponseRedirect('/set-up/add-institution-type/')

		
		except Exception as e:	
			print(e)		 
			messages.info(req, "uncaught Exception")
			return HttpResponseRedirect('/set-up/add-institution-type/')		
		
	else:
		print(form.errors)
		messages.info(req, "invalid form fields")
		return HttpResponseRedirect('/set-up/add-institution-type/')




def check_if_user_name_already_exist(req):
	pass
	# form = CleanSingleFieldForm(req.POST)

	# if req.is_ajax():	

	# 	if form.is_valid():
	# 		user_name = form.cleaned_data.get("user_name")

	# 		try:
	# 			User.objects.get(user_name = user_name)
				
	# 		except User.DoesNotExist:
	# 			 pass
	# 	else:
	# 		pass
	# else:
	# 	pass




