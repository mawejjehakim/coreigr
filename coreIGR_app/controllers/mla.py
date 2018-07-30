from django.shortcuts import render
from coreIGR_app.forms import TinNumberForm, PlateNumberForm, VehicleForm
from coreIGR_app.models import AssignedTin, Company, Individual, AssignedNumberPlate, Office, User, Vehicle, TransactionAssessment
from django.http import HttpResponseRedirect
from coreIGR_app.controllers.generate_assessment_bill import generate_assessment_bill
 
 
from random import randint
from dateutil.relativedelta import relativedelta
from datetime import date


from django.contrib import messages

today = date.today()
expirationdate_1year = today + relativedelta(years=1)



def get_tin_information(req):
	form = TinNumberForm(req.POST)

	if form.is_valid(): 
		tin_number = form.cleaned_data.get("tin")
		existing_tin =  AssignedTin.objects.filter(tin = tin_number)

		 

		if existing_tin.exists():
			if len(existing_tin) >1: 
				messages.info(req, "This Tin has multiple registraions attached to it")
				return HttpResponseRedirect('/mla/get-tin-info/')
			else:
				existing_tin_number =  existing_tin.first()
				vehicle_category = req.POST.get("vehicle_category")
				if existing_tin_number.tin_for == "Company":
					try:
						company = Company.objects.get(tin = existing_tin_number.id)
						 
						if vehicle_category ==  "Private Vehicle Saloon" or vehicle_category == "Commercial Vehicle Saloon" or vehicle_category == "Private Pickup/Bus" or vehicle_category == "Commercial Pickup/Bus" or vehicle_category == "Dealers Vehicle":
							engine_size = True
							no_of_tyres = False
							engine_category = False

							
						elif vehicle_category == "Commercial Truck/Trailer/Lorry/Tipper":
							no_of_tyres = True
							engine_size = False
							engine_category = False

							

						elif vehicle_category == "Commercial Tricycle/Motorcycle" or vehicle_category == "Private Motorcycle" or vehicle_category == "Dealers Tricycle/Motorcycle":
							engine_category = True
							no_of_tyres = False
							engine_size = False

						tin = company.tin
						local_government = company.local_government
						bussiness_status = company.bussiness_status
						bussiness_class = company.bussiness_class
						registration_number = company.registration_number
						bussiness_name = company.bussiness_name
						bussiness_owner = company.bussiness_owner

						return render(req, 'add_vehicle.html', {'current_owner_tin':tin.tin,'vehicle_category':vehicle_category,   'local_government':local_government, 'bussiness_status':bussiness_status, 'registration_number':registration_number, 'bussiness_name':bussiness_name, 'bussiness_owner':bussiness_owner, "register_for":"company"}) 

					except Company.DoesNotExist:
						 
						messages.info(req, "Tin Does Not Exist")
						return HttpResponseRedirect('/mla/get-tin-info/')
					
				else:
					try:
						 
						individual = Individual.objects.get(tin = existing_tin_number.id)

						if vehicle_category ==  "Private Vehicle Saloon" or vehicle_category == "Commercial Vehicle Saloon" or vehicle_category == "Private Pickup/Bus" or vehicle_category == "Commercial Pickup/Bus" or vehicle_category == "Dealers Vehicle":
							engine_size = True
							no_of_tyres = False
							engine_category = False

							
						elif vehicle_category == "Commercial Truck/Trailer/Lorry/Tipper":
							no_of_tyres = True
							engine_size = False
							engine_category = False

							

						elif vehicle_category == "Commercial Tricycle/Motorcycle" or vehicle_category == "Private Motorcycle" or vehicle_category == "Dealers Tricycle/Motorcycle":
							engine_category = True
							no_of_tyres = False
							engine_size = False

						tin = individual.tin
						name = individual.name
						gender = individual.gender
						state = individual.state
						address = individual.address
						occupation = individual.occupation

						  
						return render(req, 'add_vehicle.html', {'vehicle_category':vehicle_category, 'current_owner_tin':tin.tin, 'name':name, 'gender':gender, 'state':state, 'address':address, 'occupation':occupation, "register_for":"individual"}) 

					except Individual.DoesNotExist:
						 
						messages.info(req, "Tin Does Not Exist")
						return HttpResponseRedirect('mla/get-tin-info/')
		else:
			print("tin is wrong")
			messages.info(req, "Tin Does Not Exist", extra_tags = "wrong_tin")
			return HttpResponseRedirect('/mla/get-tin-info/')


	
	else:
		print(form.errors)
		messages.info(req, "invalid form fields")
		return HttpResponseRedirect('/mla/get-tin-info/')



def v_data_preview(req):
	signed_in_user_id = req.session.get("user_id")

	form = VehicleForm(req.POST)


	if form.is_valid():

		current_owner_tin = req.POST.get('current_owner_tin')

		chassis_number = form.cleaned_data.get("chassis_number")
		vehicle_model = form.cleaned_data.get("vehicle_model")
		number_plate = form.cleaned_data.get("number_plate")
		vehicle_category = form.cleaned_data.get("vehicle_category")
		gross_weight = form.cleaned_data.get("gross_weight")
		net_weight = form.cleaned_data.get("net_weight")
		no_of_passengers = form.cleaned_data.get("no_of_passengers")
		colour = form.cleaned_data.get("colour")			 
		engine_size = form.cleaned_data.get("engine_size")
		cost_price = form.cleaned_data.get("cost_price", 0)

		weight = int(gross_weight) - int(net_weight)

		try:
			staff_obj = User.objects.get(id = signed_in_user_id)
			office_obj = Office.objects.get(id = staff_obj.office.id)

						 
			# assigned_plate =  AssignedNumberPlate.objects.get(number_plate = number_plate, is_issued = False, office = office_obj.id) in coment for prodcution
			assigned_plate =  AssignedNumberPlate.objects.get(number_plate = number_plate, is_issued = True, office = office_obj.id)		

			data_context = {'current_owner_tin':current_owner_tin, 'chassis_number':chassis_number, 'vehicle_model':vehicle_model, 'number_plate':assigned_plate, 'vehicle_category':vehicle_category, 'gross_weight':gross_weight, 'net_weight':net_weight, 'no_of_passengers':no_of_passengers, 'colour':colour, 'weight':weight, 'engine_size':engine_size, 'cost_price':cost_price }
			messages.success(req, " Record Preview ",  extra_tags = 'v_data_preview data' )
			return render(req, 'add_vehicle.html', data_context)
	 	

		except AssignedNumberPlate.DoesNotExist as e:
						 
			messages.info(req, "Number Plate is wrong", extra_tags = "p_not_assigned")
			return render(req, 'add_vehicle.html')

		except Office.DoesNotExist as e:			 
			messages.info(req, "Number Plate is wrong")
			return HttpResponseRedirect('/mla/get-tin-info/')

		except Exception as e:
			print(e)				 
			messages.info(req, "Un Caught Exception")
			return HttpResponseRedirect('/mla/get-tin-info/')		
		
	else:
		print(form.errors)

		if form['number_plate'].errors: 
			messages.info(req, "Number Already resgistered", extra_tags = "p_not_assigned")
			return render(req, 'add_vehicle.html')

		elif form['chassis_number'].errors: 
			messages.info(req, "Number Already resgistered", extra_tags = "chassis_duplicate")
			return render(req, 'add_vehicle.html')

		# check if chasis is alredy registred and plate number
		messages.info(req, "invalid form fields")
		return HttpResponseRedirect('/mla/get-tin-info/')


def add_new_vehicle(req):

	signed_in_user_id = req.session.get("user_id")

	current_owner_tin = req.POST.get('current_owner_tin')
	chassis_number = req.POST.get("chassis_number")
	vehicle_model = req.POST.get("vehicle_model")
	number_plate = req.POST.get("number_plate")
	vehicle_category = req.POST.get("vehicle_category")
	gross_weight = req.POST.get("gross_weight")
	net_weight = req.POST.get("net_weight")
	weight = req.POST.get("weight")
	no_of_passengers = req.POST.get("no_of_passengers")
	colour = req.POST.get("colour")			 
	engine_size = req.POST.get("engine_size")
	cost_price = req.POST.get("cost_price", 0)

	staff_obj = User.objects.get(id = signed_in_user_id)

	add_with_particulars = req.POST.get("add_with_particulars", False)

	print(add_with_particulars)

	office_obj = Office.objects.get(office_name = staff_obj.office.office_name)

	taken_number_plate =  AssignedNumberPlate.objects.get(number_plate = number_plate)

  
	current_owner_tin = AssignedTin.objects.get(tin = current_owner_tin)

	# Vehicle.objects.create( current_owner_tin= current_owner_tin, chassis_number = chassis_number,  vehicle_model = vehicle_model,number_plate = number_plate, vehicle_category = vehicle_category, gross_weight =gross_weight , net_weight = net_weight, no_of_passengers = no_of_passengers, colour = colour, weight = weight, engine_size =engine_size, cost_price = cost_price, staff = staff_obj, office = office_obj)
	
	if add_with_particulars:
		tcode = generate_assessment_bill(req, current_owner_tin.tin, vehicle_category, engine_size, cost_price, chassis_number, staff_obj, office_obj)

		if 'correct_charge' in req.session:
			Vehicle.objects.create( current_owner_tin= current_owner_tin, chassis_number = chassis_number,  vehicle_model = vehicle_model,number_plate = number_plate, vehicle_category = vehicle_category, gross_weight =gross_weight , net_weight = net_weight, no_of_passengers = no_of_passengers, colour = colour, weight = weight, engine_size =engine_size, cost_price = cost_price, staff = staff_obj, office = office_obj)
			transaction_assessments =  TransactionAssessment.objects.filter(transaction_code = tcode)
			taken_number_plate.is_issued = True
			messages.success(req, "Vehicle Record Created", extra_tags= "assessment_prev_record_created")
			 
			print(transaction_assessments)
			print(tcode)

			return render(req, 'add_vehicle.html', {'transaction_code':tcode, 'transaction_assessments':transaction_assessments, 'vehicle_category':vehicle_category, 'vehicle_model':vehicle_model,'current_owner_tin':current_owner_tin.tin, 'chassis_number':chassis_number,})
			 
		
		else:			 
			return HttpResponseRedirect('/mla/get-tin-info/')
		
 
	else:
		Vehicle.objects.create( current_owner_tin= current_owner_tin, chassis_number = chassis_number,  vehicle_model = vehicle_model,number_plate = number_plate, vehicle_category = vehicle_category, gross_weight =gross_weight , net_weight = net_weight, no_of_passengers = no_of_passengers, colour = colour, weight = weight, engine_size =engine_size, cost_price = cost_price, staff = staff_obj, office = office_obj)
		taken_number_plate.is_issued = True
		messages.success(req, "Vehicle Record Created", extra_tags= "record_created")
		return HttpResponseRedirect('/mla/get-tin-info/')	
	
 

def get_tin_information_ch_ownership(req):
	form = ChassiNumberFieldForm(req.POST)

	if form.is_valid(): 
		tin_number = form.cleaned_data.get("chassis_number")

		try:
			vehicle = Vehicle.objects.get(chassis_number = chassis_number)

			if vehicle.theft_status:
				messages.success(req, "Vehicle is stolen ", extra_tags= "stolen vehicle")
				return render(req, 'get_tin_info_ch_ownership.html')
			
			else:
				current_owner_tin = AssignedTin.objects.get(tin_number = vehicle.current_owner_tin)

				registration_date = vehicle.registration_date
				chassis_number = vehicle.chassis_number
				vehicle_model  = vehicle.vehicle_model
				number_plate = vehicle.number_plate
				vehicle_category = vehicle.vehicle_category
				gross_weight  = vehicle.gross_weight
				net_weight = vehicle.net_weight
				no_of_passengers = vehicle.no_of_passengers
				colour = vehicle.colour
				weight = vehicle.weight
				engine_size = vehicle.engine_size
				cost_price = vehicle.cost_price
				 
				

				if current_owner_tin.tin_for == "Individual":
					individual = Individual.objects.filter(tin = current_owner_tin.tin)[0]
					
					name = individual.name
					gender = individual.gender
					state = individual.state
					address = individual.address
					email = individual.email

					 
					return render(req, 'view_to_change_vehicle_ownership.html', {"vehicle_for":"individual",
						'registration_date':registration_date, 'chassis_number':chassis_number, 'vehicle_model':vehicle_model, 
						'number_plate':number_plate, 'vehicle_category':vehicle_category, 'gross_weight':gross_weight, 'net_weight':net_weight,
						 'no_of_passengers':no_of_passengers, 'colour':colour, 'weight':weight, 'engine_size':engine_size, 'cost_price':cost_price,
						 'name':name, 'gender':gender, 'state':state, 'address':address, 'email':email } )	

					
					
				else:
					company  = Company.objects.filter(tin = current_owner_tin.tin)
					 
					local_government = company.local_government
					institution_type = company.institution_type
					bussiness_ownership_type = company.bussiness_ownership_type
					tin = company.tin
					bussiness_name = company.bussiness_name
					bussiness_address = company.bussiness_address
				 
					return render(req, 'view_to_change_vehicle_ownership.html', {"vehicle_for":"company",
						'registration_date':registration_date, 'chassis_number':chassis_number, 'vehicle_model':vehicle_model, 
						'number_plate':number_plate, 'vehicle_category':vehicle_category, 'gross_weight':gross_weight, 'net_weight':net_weight,
						 'no_of_passengers':no_of_passengers, 'colour':colour, 'weight':weight, 'engine_size':engine_size, 'cost_price':cost_price, 
						 'local_government':local_government, 'institution_type':institution_type, 'bussiness_ownership_type':bussiness_ownership_type, 'tin':tin, 'bussiness_name':bussiness_name, 'bussiness_address':bussiness_address } )	
										

				
			 


		except Vehicle.DoesNotExist:
			messages.success(req, "Vehicle Record Created", extra_tags= "wrong chasis number")
			return render(req, 'get_tin_info_ch_ownership.html')	
	else:
		print(form.errors)






	

def get_tin_information_ch_ownership(req):
	form = ChassiNumberFieldForm(req.POST)

	if form.is_valid(): 
		tin_number = form.cleaned_data.get("chassis_number")

		try:
			vehicle = Vehicle.objects.get(chassis_number = chassis_number)

			if vehicle.theft_status:
				messages.success(req, "Vehicle is stolen ", extra_tags= "stolen vehicle")
				return render(req, 'get_tin_info_ch_ownership.html')
			
			else:
				current_owner_tin = AssignedTin.objects.get(tin_number = vehicle.current_owner_tin)

				registration_date = vehicle.registration_date
				chassis_number = vehicle.chassis_number
				vehicle_model = vehicle.vehicle_model
				number_plate = vehicle.number_plate
				vehicle_category = vehicle.vehicle_category
				gross_weight  = vehicle.gross_weight
				net_weight = vehicle.net_weight
				no_of_passengers = vehicle.no_of_passengers
				colour = vehicle.colour
				weight = vehicle.weight
				engine_size = vehicle.engine_size
				cost_price = vehicle.cost_price
				 
				

				if current_owner_tin.tin_for == "Individual":
					individual = Individual.objects.filter(tin = current_owner_tin.tin)[0]
					
					name = individual.name
					gender = individual.gender
					state = individual.state
					address = individual.address
					email = individual.email

					 
					return render(req, 'view_to_change_vehicle_ownership.html', {"vehicle_for":"individual",
						'registration_date':registration_date, 'chassis_number':chassis_number, 'vehicle_model':vehicle_model, 
						'number_plate':number_plate, 'vehicle_category':vehicle_category, 'gross_weight':gross_weight, 'net_weight':net_weight,
						 'no_of_passengers':no_of_passengers, 'colour':colour, 'weight':weight, 'engine_size':engine_size, 'cost_price':cost_price,
						 'name':name, 'gender':gender, 'state':state, 'address':address, 'email':email } )	

					
					
				else:
					company  = Company.objects.filter(tin = current_owner_tin.tin)
					 
					local_government = company.local_government
					institution_type = company.institution_type
					bussiness_ownership_type = company.bussiness_ownership_type
					tin = company.tin
					bussiness_name = company.bussiness_name
					bussiness_address = company.bussiness_address
				 
					return render(req, 'view_to_change_vehicle_ownership.html', {"vehicle_for":"company",
						'registration_date':registration_date, 'chassis_number':chassis_number, 'vehicle_model':vehicle_model, 
						'number_plate':number_plate, 'vehicle_category':vehicle_category, 'gross_weight':gross_weight, 'net_weight':net_weight,
						 'no_of_passengers':no_of_passengers, 'colour':colour, 'weight':weight, 'engine_size':engine_size, 'cost_price':cost_price, 
						 'local_government':local_government, 'institution_type':institution_type, 'bussiness_ownership_type':bussiness_ownership_type, 'tin':tin, 'bussiness_name':bussiness_name, 'bussiness_address':bussiness_address } )	
										

				
			 


		except Vehicle.DoesNotExist:
			messages.success(req, "Vehicle Record Created", extra_tags= "wrong chasis number")
			return render(req, 'get_tin_info_ch_ownership.html')	
	else:
		print(form.errors)



def get_plate_information_mark_stolen(req):
	form = PlateNumberForm(req.POST)

	if form.is_valid():
		number_plate = form.cleaned_data.get("number_plate")

		try:
			vehicle_obj =  Vehicle.objects.get(number_plate = number_plate)
			render(req, 'plate_info_mark_stolen.html', {'vehicle_obj':vehicle_obj})
			
		except Vehicle.DoesNotExist:
			render(req, 'get_plate_info_mark_stolen.html')
			 
	else:
		print(form.errors)
		render(req, 'get_plate_info_mark_stolen.html')

 
def t_code():
	range_start = 10**(8-1)
	range_end = (10**8)-1
	generated_rand_num =  randint(range_start, range_end)
	tcode = "ML"+str(generated_rand_num)

	return tcode
	


def get_learners_permit(req):
	form = TinForm(req.POST)
	if form.is_valid():
		individual_tin_number = form.cleaned_data.get("individual_tin_number")

		try:
			individal_obj =  Individual.objects.get(tin = individual_tin_number)

			transaction_code = t_code
			issue_date = today
			expiration_date = expirationdate_1year

			name = individal_obj.tin		
			name = individal_obj.name
			gender = individal_obj.gender
			state = individal_obj.state
			address = individal_obj.address
			email = individal_obj.email
			phone = individal_obj.phone
 




			render(req, 'get_learners_permit.html', {'individal_obj':individal_obj})
			
		except Individual.DoesNotExist:
			render(req, 'get_tin_info_learners_permit.html')			 

			 
	else:
		print(form.errors)
		render(req, 'get_tin_info_learners_permit.html')

def save_learners_permit(req):

	form = TinForm(req.POST)
	if form.is_valid():
		individual_tin_number = form.cleaned_data.get("individual_tin_number")

		 
		transaction_code = form.cleaned_data.get('t_code')
		issue_date = form.cleaned_data.get('today')
		expiration_date = form.cleaned_data.get('expirationdate_1year')

		tin = form.cleaned_data.get('tin')
		name = form.cleaned_data.get('name')		
		 
		gender = form.cleaned_data.get('gender')
		state =form.cleaned_data.get('state')
		address =form.cleaned_data.get('address')
		email = form.cleaned_data.get('email')
		phone = form.cleaned_data.get('phone')
		options = form.cleaned_data.get('options')

		try:
			office_obj = Office.objects.get(id = id)
			user_obj = User.objects.get(id = id)

			# check if expiration date has not epired

			LearnersPermit.object.get(tin = tin, status = "is_active")


			charge_others_learners_permit =	ChargesOthers.objects.get( particulars = 'Learners Permit')				
			learners_permit = charge_others_learners_permit.amount

			charge_others_lsymbol = ChargesOthers.objects.get( particulars='L-Symbol' )				
			lsymbol_amount = charge_others_lsymbol.amount

			#Get sms amount
			charge_others_sms_amount = ChargesOthers.objects.get( particulars='SMS Alert' )				
			sms_amount = charge_others_sms_amount.amount

			#Get Stamp Duty Amount
			charge_others_stamp_duty = ChargesOthers.objects.get( particulars='Stamp Duty')				
			stamp_amount = charge_others_stamp_duty.amount
		 

			#Save record
			LearnersPErmit.objects.create(status = "Active", tcode = transaction_code, tin = tin, name = name, gender = gender, address = address, phone = phone, issue_date = issue_date, expiration_date = expiration_date, particulars = options, Amount = amount, staff = staff_obj, office = office_obj) 
				                         

			if(options == "Permit Only"):
				particulars = "Learners Permit"
				amount = learners_permit
				#SAVE INTO ASSESSMENT TRANSACTION
				TransactionAssessment.objects.create(tcode = transaction_code, tin = tin, particulars = particulars, amount = amount, issue_date = issue_date, expiration_date =  expiration_date, transaction_type = 'Learners Permit', payment_status = 'Not Paid', transaction_staff = staff, transaction_office = office_obj) 
				                         

				particulars = "SMS Alert"
				amount = sms_amount
					#SAVE INTO ASSESSMENT TRANSACTION
				TransactionAssessment.objects.create(status = "Active", tcode = transaction_code, tin = tin, name = name, gender = gender, address = address, phone = phone, issue_date = issue_date, transaction_type = 'SMS Alert', payment_status = 'Not Paid',transaction_staff = staff, transaction_office = office_obj) 
				                         

				particulars = "Stamp Duty"
				amount = stamp_amount
					#SAVE INTO ASSESSMENT TRANSACTION
				TransactionAssessment.objects.create(status = "Active", tcode = transaction_code, tin = tin, name = name, gender = gender, address = address, phone = phone, issue_date = issue_date,  transaction_type = 'Stamp Duty', payment_status = 'Not Paid',transaction_staff = staff, transaction_office = office_obj) 
				                           


				
			elif(options == "Permit and L-Symbol"):
				particulars = "Learners Permit + L-Symbol"
				amount = learnerspermit + lsymbol
				#SAVE INTO ASSESSMENT TRANSACTION
				TransactionAssessment.objects.create(status = "Active", tcode = transaction_code, tin = tin, name = name, gender = gender, address = address, phone = phone, issue_date = issue_date, transaction_type = 'Learners Permit', payment_status = 'Not Paid',transaction_staff = staff, transaction_office = office_obj) 
				                            

				particulars = "SMS Alert"
				amount = sms_amount
				#SAVE INTO ASSESSMENT TRANSACTION
				TransactionAssessment.objects.create(status = "Active", tcode = transaction_code, tin = tin, name = name, gender = gender, address = address, phone = phone, issue_date = issue_date, transaction_type = 'SMS Alert', payment_status = 'Not Paid',transaction_staff = staff, transaction_office = office_obj) 
				                      

				particulars = "Stamp Duty"
				amount = stamp_amount
				#SAVE INTO ASSESSMENT TRANSACTION
				TransactionAssessment.objects.create(status = "Active", tcode = transaction_code, tin = tin, name = name, gender = gender, address = address, phone = phone, issue_date = issue_date, transaction_type = 'Stamp Duty', payment_status = 'Not Paid',transaction_staff = staff, transaction_office = office_obj) 
				                            


				messages.info(req, "record added Successfully")
				return render(req, 'get_tin_info_learners_permit.html')
		except LearnersPermit.DoesNotExist as e:
			print(e)
			return render(req, 'get_tin_info_learners_permit.html')	

		except Exception as e:
			print(e)
			return render(req, 'get_tin_info_learners_permit.html')	

	else:
		print(form.errors)

def vehicle_revalidation(req):
	form = ChassisNumberFieldForm(req.POST)
	if form.is_valid():
		chassis_number = form.cleaned_data.get("chassis_number")

		try:
			vehicle_obj =  Vehicle.objects.get(chassis_number = chassis_number)

			 

			# owners_tin = vehicle_obj.tin		
			# vehicle_type = vehicle_obj.vehicle_type
			# vehicle_category = vehicle_obj.vehicle_category
			# chassis_number = vehicle_obj.chassis_number
			# number_plate = vehicle_obj.number_plate
			# engine_size = vehicle_obj.engine_size
			# cost_price = vehicle_obj.cost_price

			individal_obj = Individual.objects.get(tin = owners_tin)

			owners_name = individal_obj.name
			chassis_number = req.session['chassis_number']
 

			render(req, 'view_to_change_vehicle_revalidation.html', {'vehicle_obj':vehicle_obj, 'owners_name':owners_name})
			
		except Vehicle.DoesNotExist:
			render(req, 'get_tin_info_revalidation.html')		 

			 
	else:
		print(form.errors)
		render(req, 'get_tin_info_revalidation.html')


def save_revalidation(req):
	form = ChassisNumberFieldForm(req.POST)
	if form.is_valid():
		plate_number = form.cleaned_data.get("plate_number")
		chassis_number = req.session.get('chassis_number')

		try:
			vehicle_obj =  Vehicle.objects.get(chassis_number = chassis_number, tin = current_owner_tin)
			Revalidation.objects.create(tin = individal_obj.tin, name = individal_obj.name, old_plate_no = vehicle_obj.old_plate_no, new_plate_no = plate_number)

			vehicle_obj.number_plate = new_plate_no
			vehicle_obj.save()

			 # t_code()

			if(vehicle_category == "Private Vehicle Saloon" or vehicle_category == "Private Pickup/Bus" or  vehicle_category == "Commercial Vehicle Saloon" or  vehicle_category == "Commercial Pickup/Bus" or  	vehicle_category == "Commercial Truck/Trailer/Lorry/Tipper"):
			 	charge_others =  ChargesOthers.objects.get( particulars ='New Plate Number' )
			 	amount = charge_others.amount

			else:
				charge_others =  ChargesOthers.objects.get(particulars ='New Plate Number (TM)' )

				amount = charge_others.amount
				particulars = "New Plate Number"
				transactionType = "Revalidation" 


				# SAVE INTO ASSESSMENT TRANSACTION
				TransactionAssessment.objects.create( tcode = tcode, tin = tin, chassis = chassis_number, particulars = particulars, amount = amount, transaction_type = 'Revalidation', payment_status = 'Not Paid', transaction_staff = staff, transaction_office = office_obj) 
				
				if(vehicle_category == "Private Vehicle Saloon"):
					return revalid_ps 
						
				elif(vehicle_category == "Commercial Vehicle Saloon"):
					return revalid_cvs 
						
				elif(vehicle_category == "Private Pickup/Bus"):
					return revalid_ppb 
					
				elif(vehicle_category == "Commercial Pickup/Bus"):
					return revalid_cpb 
					
				elif(vehicle_category == "Commercial Truck/Trailer/Lorry/Tipper"):
					return revalid_ct 
					
				elif(vehicle_category == "Commercial Tricycle/Motorcycle"):
					return revalid_tm 
					
				elif(vehicle_category == "Private Motorcycle"):
					return revalid_pm 
				


				# Transaction_Code'] = tcode
				# new_owner'] = name
				# new_owner_tin'] = tin

 

			render(req, 'view_to_change_vehicle_revalidation.html')
			
		except Vehicle.DoesNotExist:
			render(req, 'get_tin_info_revalidation.html')		 

			 
	else:
		print(form.errors)
		render(req, 'get_tin_info_revalidation.html')

 
def get_vehicle_assessment(req): 
	form = VehicleAssessmentForm(req.POST)
	if form.is_valid():
	 
		search_text = form.cleaned_data.get('search_text')

		if len(search_text) > 8:
			# chassis_number
			try:
				vehicle_obj = Vehicle.objects.get(chassis = search_text)
				chas = vehicle_obj.chassis
				
				if(vehicle_obj.mark == "stolen"):
					# vehicle stoen
					messages.info(req, "this car is stolen")
					return render(req, 'get_tin_info_renewal.html')	

				else:

					tin = vehicle_obj.tin_current_owner
					chassis = vehicle_obj.chassis
					vehicle_type = vehicle_obj.vehicle_type
					number_plate = vehicle_obj.number_plate
					category = vehicle_obj.category
					gross_weight = vehicle_obj.gross_weight
					net_weight = vehicle_obj.net_weight
					persons = vehicle_obj.persons
					color = vehicle_obj.color
					weight_carry = vehicle_obj.weight
					engine_size = vehicle_obj.engine_size
					cost_price = vehicle_obj.cost_price

					individal_obj =  Individual.objects.get(tin= tin )
				 
					transcode = req.seesino.renew_transaction_code
					 
					invoice_code = transcode
					invoice_tin = tin 
					invoice_chassis = chassis
					invoice_name  = individal_obj.name
					invoice_model = vehicle_type
					invoice_category  = category
					
					transaction_assessments = TransactionAssessment.objects.filter(tcode = transcode, tdate = date)

					return render(req, 'vehicle_assessment.html', {'vehicle_obj':vehicle_obj, 'transaction_assessments':transaction_assessments})		 
			except:
				return render(req, 'get_tin_info_renewal.html')	

			 
			 
			
		else:
			try:
				vehicle_obj = Vehicle.objects.get(number_plate = search_text)
				chassis = vehicle_obj.chassis
				
				if(vehicle_obj.mark == "stolen"):
					# vehicle stoen
					return render(req, 'get_tin_info_renewal.html')	

				else: 

					tin = vehicle_obj.tin_current_owner
					chassis = vehicle_obj.chassis
					vehicle_type = vehicle_obj.vehicle_type
					number_plate = vehicle_obj.number_plate
					category = vehicle_obj.category
					gross_weight = vehicle_obj.gross_weight
					net_weight = vehicle_obj.net_weight
					persons = vehicle_obj.persons
					color = vehicle_obj.color
					weight_carry = vehicle_obj.weight
					engine_size = vehicle_obj.engine_size
					cost_price = vehicle_obj.cost_price

					individal_obj =  Individual.objects.get(tin= tin )
				 
					transcode = req.seesino.renew_transaction_code
					 
					invoice_code = transcode
					invoice_tin = tin 
					invoice_chassis = chassis
					invoice_name  = individal_obj.name
					invoice_model = vehicle_type
					invoice_category  = category
					transaction_assessments = TransactionAssessment.objects.filter(tcode = transcode, tdate = date)

					return render(req, 'vehicle_assessment.html', {'vehicle_obj':vehicle_obj, 'transaction_assessments':transaction_assessments})	
			except:
				return render(req, 'get_tin_info_renewal.html')	
			

		

def save_assessment(req):
	form = VehicleAssementForm(req.POST)
	if form.is_valid():
		assessment_type = form.cleaned_data.get("assessment_type")
		
		try:
			tcode = req.session.get(renew_transaction_code)			 
			transaction_assessments = TransactionAssessment.objects.get(tcode ='tcode',  particulars = assessment_type )

			messages.info(req, "already exist print")
			return render(req, 'get_tin_info_revalidation.html')


		 
				 
		except TransactionAssessment.DoesNotExist:

			if(category == "Private Vehicle Saloon"):
				return renew_ps
				
			elif( category == "Commercial Vehicle Saloon"):
				return renew_cvs
				
			elif( category == "Private Pickup/Bus"):
				return renew_ppb
				
			elif( category == "Commercial Pickup/Bus"):
				return renew_cpb

			elif( category == "Commercial Truck/Trailer/Lorry/Tipper"):
				return renew_ct
				
			elif( category == "Commercial Tricycle/Motorcycle"):
				return renew_tm
				
			elif( category == "Private Motorcycle"):
				return renew_pm

			elif( category == "Dealers Vehicle"):
				return renew_dv
				
			elif( category == "Dealers Tricycle/Motorcycle"):
				return renew_dtm
		except Exception as e:
			print(e)

