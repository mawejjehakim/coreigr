from django.shortcuts import render
from coreIGR_app.controllers.set_up import user_login, add_new_user, check_if_user_name_already_exist, add_new_office, add_new_lga, add_new_state_code, add_new_charge, add_new_institution_category, add_new_institution_type
from django.contrib import messages
from coreIGR_app.controllers.tin import save_new_individual, i_data_preview, c_data_preview, save_new_company
from django.http import HttpResponseRedirect
from coreIGR_app.models import User, Office, LocalGovArea, StateCode, Charge, Company, Individual, InstitutionType, InstitutionCategory, Vehicle, NumberPlate, MDA, AssignedTin, AssignedNumberPlate
from coreIGR_app.controllers.mla  import get_tin_information, v_data_preview, get_tin_information_ch_ownership, get_plate_information_mark_stolen, get_learners_permit, vehicle_revalidation
from coreIGR_app.controllers.store import p_n_data_preview, save_new_plate_number, get_localgov_numberplates
from coreIGR_app.controllers.mda import add_new_mda
	 
def login(req):
	return user_login(req)

def add_user(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":
			offices = Office.objects.all()	 

			if req.method == "GET":			
				return render(req, 'add_user.html', {"offices":offices})

			elif req.method == "POST" and req.POST:				 
				return add_new_user(req)
				
			else:				
				return render(req, 'add_user.html', {"offices":offices})				 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")
			return HttpResponseRedirect('/login/')
			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "singn in")		 
		return HttpResponseRedirect('/login/')

		# okay this


def add_office(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":
				
				return render(req, 'add_office.html')

			elif req.method == "POST" and req.POST:				 
				return add_new_office(req)
				
			else:
				HttpResponseRedirect('/set-up/add-office/')				 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")
			return HttpResponseRedirect('/login/')
			
	else:
		messages.info(req, "singn in")		 
		return HttpResponseRedirect('/login/')





def all_users(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == 'Super Administrator':			 
			users = User.objects.all()
			
			return render(req, 'users.html', {"users":users})				
			 
		else:			 
			messages.info(req, "You dont have the right to perform this operation")
			return HttpResponseRedirect('/login/')
		
	else:
		messages.info(req, "Sign in Please")
		return HttpResponseRedirect('/login/')



def all_lgas(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):


		if user_access_level == 'Super Administrator':
			 
			lgas = LocalGovArea.objects.all()	

			try:
				state_code_obj = StateCode.objects.get(id = 1)
				state_code = state_code_obj.state_code
				state_code_value = state_code_obj.state_code
				return render(req, 'lga.html', { "lgas":lgas, "state_code":state_code, "state_code_value":state_code_value})
					
			except StateCode.DoesNotExist:
				state_code = "Set new State Code"
				state_code_value = "#"
				return render(req, 'lga.html', { "lgas":lgas, "state_code":state_code, "state_code_value":state_code_value})
		
							
			 
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "Sign in Please")
		return render(req, 'login.html')

def add_lga(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":

				return render(req, 'add_LGA.html')

			elif req.method == "POST" and req.POST:				 
				return add_new_lga(req)
				
			else:
				messages.success(req, "add lga")
				HttpResponseRedirect('/set-up/add-lga/')				 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')

def save_state_code(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":
				 			
				return HttpResponseRedirect('/set-up/lgas')

			elif req.method == "POST" and req.POST:				 
				return add_new_state_code(req)
				
			else:
				 
				return HttpResponseRedirect('/set-up/lgas/')				 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')

def search_record(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":
				return render(req, "search_results.html", {"msg":"Please type in a correct tin in a search field to search for a record"})	

			elif req.method == "POST" and req.POST:

				try:
					search_text = req.POST.get("search_text")
					tin_record_obj = AssignedTin.objects.filter(tin = search_text)

					if tin_record_obj.exists():

						existing_tin = tin_record_obj.first()
						if existing_tin.tin_for == "Company":
							 

							company_obj = Company.objects.filter(tin = existing_tin.id)
							return render(req, "search_results.html", {"search_results":company_obj, "for":"company"})

						else:
							 
							individual_obj = Individual.objects.filter(tin = existing_tin.id)
							print(individual_obj)
							return render(req, "search_results.html", {"search_results":individual_obj, "for":"individual"})

					else:
						print("no records atteched to this tin")
						return render(req, "search_results.html", {"msg":"No records found "})

						

					 
				except Exception as e:
					print (e)
					return render(req, "search_results.html")	
						
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')




def all_offices(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):


		if user_access_level == 'Super Administrator':

			offices = Office.objects.all()	 

			return render(req, 'offices.html', {"offices":offices})				
			 
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "Sign in Please")
		return render(req, 'login.html')


def all_charges(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):


		if user_access_level == 'Super Administrator':
			 
			charges = Charge.objects.all()
		 
			return render(req, 'charges.html', {"charges":charges})				
			 
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "Sign in Please")
		return render(req, 'login.html')

def add_charge(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":
								
				return render(req, 'add_charge.html')

			elif req.method == "POST" and req.POST:				 
				return add_new_charge(req)
				
			else:
				messages.success(req, "add state code")
				return render(req, 'add_charge.html')			 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')



 
def all_institution_categories(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == 'Super Administrator':			 
			institution_categories = InstitutionCategory.objects.all()
			
			return render(req, 'institution_categories.html', {"institution_categories":institution_categories})				
			 
		else:			 
			messages.info(req, "You dont have the right to perform this operation")
			return HttpResponseRedirect('/login/')
		
	else:
		messages.info(req, "Sign in Please")
		return HttpResponseRedirect('/login/')


def add_institution_category(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":

				return render(req, 'add_institution_category.html')

			elif req.method == "POST" and req.POST:				 
				return add_new_institution_category(req)
				
			else:
				messages.success(req, "Add institution category")
				HttpResponseRedirect('/set-up/add-institution-category/')				 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')



def all_institution_types(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == 'Super Administrator':			 
			institution_types = InstitutionType.objects.all()
			
			return render(req, 'institution_types.html', {"institution_types":institution_types})				
			 
		else:			 
			messages.info(req, "You dont have the right to perform this operation")
			return HttpResponseRedirect('/login/')
		
	else:
		messages.info(req, "Sign in Please")
		return HttpResponseRedirect('/login/')

def add_institution_type(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":

				return render(req, 'add_institution_type.html')

			elif req.method == "POST" and req.POST:				 
				return add_new_institution_type(req)
				
			else:
				messages.success(req, "Add Institution Type")
				HttpResponseRedirect('/set-up/add-institution-type/')				 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')



def all_individuals(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):


		if user_access_level == 'Super Administrator':
			 
			individuals = Individual.objects.all()			
		 
			return render(req, 'individuals.html', {"individuals":individuals})				
			 
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "Sign in Please")
		return render(req, 'login.html')


def add_individual(req):
	user_access_level  = req.session.get("access_level")
	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":
				LGAs = LocalGovArea.objects.all()
				work_places = Company.objects.all()
		
				return render(req, 'add_individual.html', {"LGAs":LGAs, "work_places":work_places})
				
			else:
				 
				return render(req, 'add_individual.html')
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')

def i_data_preview_before_saving(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":
						
				return HttpResponseRedirect('/tin/add-individual/')

			elif req.method == "POST" and req.POST:				 
				return i_data_preview(req)
				
			else:
				
				return HttpResponseRedirect('/tin/add-individual/')				 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')

def save_individual(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":	

			if req.method == "POST" and req.POST: 		 
				return save_new_individual(req)
				
			else:
				
				return render(req, 'add_individual.html')			 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')




def all_companies(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):


		if user_access_level == 'Super Administrator':
			 
			companies = Company.objects.all()			
		 
			return render(req, 'companies.html', {"companies":companies})				
			 
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "Sign in Please")
		return render(req, 'login.html')


def add_company(req):
	user_access_level  = req.session.get("access_level")
	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":
				institution_categories = InstitutionCategory.objects.all()
				institution_types = InstitutionType.objects.all()
				LGAs = LocalGovArea.objects.all()
				
				return render(req, 'add_company.html', {"LGAs":LGAs, "institution_types":institution_types, "institution_categories":institution_categories })
			
			else:
				 
				return render(req, 'add_company.html')
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')


def c_data_preview_before_saving(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":
						
				return HttpResponseRedirect('/tin/add-company/')

			elif req.method == "POST" and req.POST:				 
				return c_data_preview(req)
				
			else:
				
				return HttpResponseRedirect('/tin/add-company/')				 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')



def save_company(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":	
			

			if req.method == "POST" and req.POST: 		 
				return save_new_company(req)
				
			else:				
				return render(req, 'add_company.html')			 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')


def get_tin_info(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":

			if req.method == "GET":
				return render(req, 'get_tin_info.html')			

			elif req.method == "POST" and req.POST: 		 
				return get_tin_information(req)
				
			else:				
				return render(req, 'get_tin_info.html')			 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')



def all_vehicles(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == 'Super Administrator':			 
			vehicles = Vehicle.objects.all()
			
			return render(req, 'vehicles.html', {"vehicles":vehicles})				
			 
		else:			 
			messages.info(req, "You dont have the right to perform this operation")
			return HttpResponseRedirect('/login/')
		
	else:
		messages.info(req, "Sign in Please")
		return HttpResponseRedirect('/login/')



def v_data_preview_before_saving(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":
						
				return HttpResponseRedirect('/mla/get-tin-info/')

			elif req.method == "POST" and req.POST:

				return v_data_preview(req)
				
			else:

				
				return HttpResponseRedirect('/mla/get-tin-info/')				 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')



def all_number_plates(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == 'Super Administrator':			 
			number_plates = NumberPlate.objects.all()
			
			return render(req, 'number_plates.html', {"number_plates":number_plates})				
			 
		else:			 
			messages.info(req, "You dont have the right to perform this operation")
			return HttpResponseRedirect('/login/')
		
	else:
		messages.info(req, "Sign in Please")
		return HttpResponseRedirect('/login/')



def add_number_plate(req):

	user_access_level  = req.session.get("access_level")
	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":
				LGAs = LocalGovArea.objects.all()
				
				return render(req, 'add_number_plate.html', {"LGAs":LGAs })
			
			else:
				 
				return render(req, 'add_number_plate.html')
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')





def p_n_data_preview_before_saving(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":
						
				return HttpResponseRedirect('/store/add-number-plate/')

			elif req.method == "POST" and req.POST:				 
				return p_n_data_preview(req)
				
			else:
				
				return HttpResponseRedirect('/store/add-number-plate/')				 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')
p_n_data_preview_before_saving




def save_number_plate(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":	
			

			if req.method == "POST" and req.POST: 		 
				return save_new_plate_number(req)
				
			else:				
				return render(req, 'add_number_plate.html')			 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')



def get_office_name(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":

			if req.method == "POST" and req.POST:

				office_name = req.POST.get("office_name")
				LGAs = LocalGovArea.objects.all()
				offices = Office.objects.all() 		
				
				req.session['sess_office_name'] = office_name

				 
				return render(req, 'assign_plate_number.html', {"office_name":office_name, "LGAs":LGAs})			

			
			else:
				offices = Office.objects.all() 
				return render(req, 'get_office_name.html', {"offices":offices})	
				
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')


def get_lgov_numberplates(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":

			if req.method == "GET":

				HttpResponseRedirect('/store/get-office-name/')

				 				
			elif req.method == "POST" and req.POST:
				return get_localgov_numberplates(req)

				
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')







def add_mda(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":
								
				return render(req, 'add_mda.html')

			elif req.method == "POST" and req.POST:				 
				return add_new_mda(req)
				
			else:
				messages.success(req, "add mda")
				return render(req, 'add_mda.html')			 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')

def all_mdas(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == 'Super Administrator':			 
			mdas = MDA.objects.all()
			
			return render(req, 'mdas.html', {"mdas":mdas})				
			 
		else:			 
			messages.info(req, "You dont have the right to perform this operation")
			return HttpResponseRedirect('/login/')
		
	else:
		messages.info(req, "Sign in Please")
		return HttpResponseRedirect('/login/')
		


def change_vehicle_ownership(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":

			if req.method == "GET":
				return render(req, 'get_tin_info_ch_ownership.html')			

			elif req.method == "POST" and req.POST: 		 
				return get_tin_information_ch_ownership(req)
				
			else:				
				return render(req, 'get_tin_info_ch_ownership.html')			 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')


def mark_stolen_vehicle(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":

			if req.method == "GET":
				return render(req, 'get_plate_info_mark_stolen.html')			

			elif req.method == "POST" and req.POST: 		 
				return get_plate_information_mark_stolen(req)
				
			else:				
				return render(req, 'get_plate_info_mark_stolen.html')			 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')

def mark_vehicle(req, plate_number):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":

			if req.method == "GET":
				vehicle_obj = Vehicle.objects.get(id = id)

				if  vehicle_obj.theft_status:
					vehicle_obj.theft_status = False
				else:
					vehicle_obj.theft_status = True

				try:
					vehicle_obj =  Vehicle.objects.get(number_plate = plate_number)
					render(req, 'plate_info_mark_stolen.html', {'vehicle_obj':vehicle_obj})
			
				except Vehicle.DoesNotExist:
					render(req, 'get_plate_info_mark_stolen.html')		
		 	 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')

def get_tin_info_revalidation(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":

			if req.method == "GET":
				return render(req, 'get_tin_info_revalidation.html')			

			elif req.method == "POST" and req.POST: 		 
				return get_learners_permit(req)
				
			else:				
				return render(req, 'get_tin_info_revalidation.html')			 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')



def save_learners_permit(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":

			if req.method == "GET":
				HttpResponseRedirect('mla/get-learners-permit')			

			elif req.method == "POST" and req.POST: 		 
				return save_learners_permit(req)
				
			 
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')



def get_chassisnumber_info_vehicle_revalidation(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":

			if req.method == "GET":
				return render(req, 'get_tin_info_revalidation.html')			

			elif req.method == "POST" and req.POST: 		 
				return vehicle_revalidation(req)
				
			else:				
				return render(req, 'get_tin_info_revalidation.html')			 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')

def check_user_name(req):
	check_if_user_name_already_exist(req)

def save_vehicle_revalidation(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":

			if req.method == "GET":
				HttpResponseRedirect('mla/change-vehicle-revalidation')			

			elif req.method == "POST" and req.POST: 		 
				return save_revalidation(req)
			
			 
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')
	

def get_chassisnumber_info_vehicle_assessment(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":

			if req.method == "GET":
				return render(req, 'get_tin_info_renewal.html')			

			elif req.method == "POST" and req.POST: 		 
				return get_vehicle_assessment(req)
				
			else:				
				return render(req, 'get_tin_info_renewal.html')			 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')


def save_vehicle_assessment(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":

			if req.method == "GET":
				HttpResponseRedirect('/mla/get-vehicle-assessment/')			

			elif req.method == "POST" and req.POST: 		 
				return save_assessment(req)
			
			 
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')



def genearate_bill(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":

			if req.method == "GET":
				return render(req, 'get_plate_info_generate_bill.html')			

			elif req.method == "POST" and req.POST: 		 
				return get_genearate_bill(req)
				
			else:				
				return render(req, 'get_plate_info_generate_bill.html')			 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')

def select_payement(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":

			if req.method == "GET":
				return render(req, 'select_payement.html')			

			 
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')

def revenue_items(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == 'Super Administrator':			 
			revenue_items = RevenueItems.objects.all()
			
			return render(req, 'revenue_items.html', {"revenue_items":revenue_items})				
			 
		else:			 
			messages.info(req, "You dont have the right to perform this operation")
			return HttpResponseRedirect('/login/')
		
	else:
		messages.info(req, "Sign in Please")
		return HttpResponseRedirect('/login/')


def edit_individual(req, individual_id):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":

			if individual_id != "":

				try:
					individual_obj =  Individual.objects.get(id = individual_id)

					work_places  = Company.objects.all()

					return render(req, 'edit_individual_record.html', {'individual_obj':individual_obj, "work_places":work_places})
					
				except Individual.DoesNotExist:
					return HttpResponseRedirect('/tin/add-individual/')
 
 
			else:
				 
				return HttpResponseRedirect('/tin/add-individual/')				 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')

def update_individual(req):

	 
	try:		
		individual_id = req.POST.get("id")
		tin = req.POST.get("tin")
		name = req.POST.get("name")
		gender = req.POST.get("gender")
		date_of_birth = req.POST.get("date_of_birth")
		marital_status = req.POST.get("marital_status")
		state = req.POST.get("state")
		address = req.POST.get("address")
		phone = req.POST.get("phone")
		email = req.POST.get("email")
		occupation = req.POST.get("occupation")
		employment_status = req.POST.get("employment_status")
		work_place = req.POST.get("work_place")

		
		individual_obj = Individual.objects.get(tin = tin)
		 
		individual_obj.name = name
		individual_obj.gender = gender
		individual_obj.date_of_birth = date_of_birth
		individual_obj.marital_status = marital_status
		individual_obj.state = state
		individual_obj.address = address
		individual_obj.phone = phone
		individual_obj.email = email
		individual_obj.occupation = occupation
		individual_obj.employment_status = employment_status
		individual_obj.work_place= work_place

		individual_obj.save()

		messages.success(req, "Individual record Updated Successfuly ", extra_tags= "record_updated")
		return HttpResponseRedirect('/tin/edit-individual/'+individual_id)

		
	except Exception as e:
		print(e)
		return HttpResponseRedirect('/tin/add-individual/')


def edit_company(req, company_id):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":

			if company_id != "":

				try:
					company_obj =  Company.objects.get(id = company_id)

					# work_places  = Company.objects.all()

					return render(req, 'edit_company_record.html', {'company_obj':company_obj} )
					
				except Individual.DoesNotExist:
					return HttpResponseRedirect('/tin/add-company/')
 
 
			else:
				 
				return HttpResponseRedirect('/tin/add-company/')				 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')


def update_company(req):

	 
	try:		
		company_id = req.POST.get("id")
		tin = req.POST.get("tin")
		institution = req.POST.get("institution")
		bussiness_status = req.POST.get("bussiness_status")
		bussiness_class = req.POST.get("bussiness_class")
		registration_number = req.POST.get("registration_number")
		bussiness_ownership_type = req.POST.get("bussiness_ownership_type")
		bussiness_name = req.POST.get("bussiness_name")
		bussiness_owner = req.POST.get("bussiness_owner")
		bussiness_address = req.POST.get("bussiness_address")
		phone_number = req.POST.get("phone_number")
		email = req.POST.get("email")
		employment_status = req.POST.get("employment_status")
		work_place = req.POST.get("work_place")
		institution_type = req.POST.get("institution_type")
		institution_category = req.POST.get("institution_category")

		
		company_obj = Company.objects.get(tin = tin)

		institution_type_obj = InstitutionType.objects.get(institution_type = institution_type)
		institution_category_obj = InstitutionCategory.objects.get(institution_category = institution_category)
		 
		company_obj.institution = institution
		company_obj.institution_type = institution_type_obj
		company_obj.institution_category = institution_category_obj
		company_obj.bussiness_status = bussiness_status
		company_obj.bussiness_class = bussiness_class
		company_obj.registration_number = registration_number
		company_obj.bussiness_ownership_type = bussiness_ownership_type
		company_obj.bussiness_name = bussiness_name
		company_obj.bussiness_owner = bussiness_owner
		company_obj.bussiness_address = bussiness_address
		company_obj.phone_number = phone_number
		company_obj.email = email
		 
		company_obj.save()

		messages.success(req, "Company record Updated Successfuly ", extra_tags= "record_updated")
		return HttpResponseRedirect('/tin/edit-company/'+company_id)

		
	except Exception as e:
		print(e)
		return HttpResponseRedirect('/tin/add-company/')


 

def edit_office(req, office_id):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":

			if office_id != "":

				try:
					office_obj =  Office.objects.get(id = office_id)

					

					return render(req, 'edit_office_record.html', {'office_obj':office_obj} )
					
				except Office.DoesNotExist:

					return HttpResponseRedirect('/set-up/add-office/')
 
 
			else:
				 
				return HttpResponseRedirect('/set-up/add-office/')				 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')


def update_office(req):
	 
	try:		
		office_id = req.POST.get("id")		 
		office_name = req.POST.get("office_name")

		office_obj = Office.objects.get(id = office_id)
  

		office_obj.office_name = office_name	 	 
		office_obj.save()

	 
		messages.success(req, "Office record Updated Successfuly ", extra_tags= "record_updated")

		 
		return HttpResponseRedirect('/set-up/edit-office/'+office_id)

		
	except Exception as e:
		print(e)
		return HttpResponseRedirect('/set-up/edit-office/'+office_id)


def enable_dis_office(req, office_id):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":

		

			try:
				office_obj =  Office.objects.get(id = office_id)

				if office_obj.is_active:
					office_obj.is_active = False
					office_obj.save()
					messages.success(req, "Office State Changed ", extra_tags= "record_state_updated")
					return HttpResponseRedirect('/set-up/offices/')
				else:
					office_obj.is_active = True
					office_obj.save()
					messages.success(req, "Office State Changed ", extra_tags= "record_state_updated")
					return HttpResponseRedirect('/set-up/offices/')
										 
				
			except Office.DoesNotExist:

				return HttpResponseRedirect('/set-up/offices/')

  			 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')




def issue_number_plate(req, plate_number):

	
	sess_office_name = req.session['sess_office_name']
	sess_lga = req.session.get("sess_lga")
	LGAs = LocalGovArea.objects.all()

				 
	office_obj = Office.objects.get(office_name = sess_office_name )
	number_plate = NumberPlate.objects.get(number_plate = plate_number)



	if not number_plate.is_issued:
		assigned_number_plate = AssignedNumberPlate.objects.create(number_plate = number_plate, office = office_obj)
		lg_number_plates = NumberPlate.objects.filter(local_government = sess_lga, is_issued=False)
		number_plate.is_issued = True
		number_plate.save() 
		issued_number_plates = AssignedNumberPlate.objects.filter( office = office_obj.id)

		return render(req, 'assign_plate_number.html', {'office_name':sess_office_name, "LGAs":LGAs, 'number_plates':lg_number_plates,'lg':sess_lga}) 

	else:
		 
		assigned_number_plate = AssignedNumberPlate.objects.get(number_plate = number_plate, office = office_obj).delete()
		lg_number_plates = NumberPlate.objects.filter(local_government = sess_lga, is_issued=False)
		 
		number_plate.is_issued = False
		number_plate.save()
		return render(req, 'assign_plate_number.html', {'office_name':sess_office_name, "LGAs":LGAs, 'number_plates':lg_number_plates,'lg':sess_lga})


 
