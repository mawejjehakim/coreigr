
from django.shortcuts import render
from random import randint

from coreIGR_app.models import  Individual, Company, StateCode, AssignedTin, User, Office, LocalGovArea, InstitutionType, InstitutionCategory
from coreIGR_app.forms import IndividualForm, CompanyForm
from django.contrib import messages


from django.http import HttpResponseRedirect


def generate_tin(req):
	 
    range_start = 10**(6-1)
    range_end = (10**6)-1
   
    local_government_area_code = req.POST.get("lga")
    generated_rand_num =  randint(range_start, range_end)
    try:
    	
    	state_code_obj = StateCode.objects.get(id=1)
    	print(local_government_area_code)
    	tin = str(state_code_obj.state_code+local_government_area_code+str(generated_rand_num))
    	return tin

    except StateCode.DoesNotExist:
    	print("set state_code first")
    	messages.info(req, "Please Set StateCode to continue")
    	HttpResponseRedirect('/tin/individuals/')   


def i_data_preview(req):

	form = IndividualForm(req.POST)

	if form.is_valid():
		
	
		try:			
			new_tin = generate_tin(req)
			if len(new_tin) == 10:					
				tin_obj = AssignedTin.objects.filter(tin = new_tin)

				while tin_obj.exists():
					new_tin = generate_tin(req)
					tin_obj = AssignedTin.objects.filter(tin = new_tin)


				title = req.POST.get("title")
				name = form.cleaned_data.get("name")
				gender = form.cleaned_data.get("gender")
				date_of_birth = form.cleaned_data.get("date_of_birth")
				marital_status = form.cleaned_data.get("marital_status")
				state = form.cleaned_data.get("state")
				address = form.cleaned_data.get("address")
				phone = form.cleaned_data.get("phone")
				email = form.cleaned_data.get("email")
				occupation = form.cleaned_data.get("occupation")
				employment_status = form.cleaned_data.get("employment_status")
				work_place = form.cleaned_data.get("work_place")

				data_context = {"tin":new_tin, 'name':title+" "+name, 'gender':gender, 'date_of_birth':date_of_birth, 'marital_status':marital_status, 'state':state, 'address':address, 'phone':phone, 'email':email, 'occupation':occupation, 'employment_status':employment_status, 'work_place':work_place }
				
				messages.success(req, " Record Preview ",  extra_tags = 'i_data_preview data' )
				return render(req, 'add_individual.html', data_context)

			else:
				print("tin cant be generated")	
				return HttpResponseRedirect('/tin/add-individual/')
				 		
		except Exception as e:
			print(e)			 
			messages.info(req, "uncaught Exception")
			return HttpResponseRedirect('/tin/add-individual/')	

		except User.DoesNotExist:					 
			messages.info(req, "uncaught Exception")
			return HttpResponseRedirect('/tin/add-individual/')	

		except Office.DoesNotExist:					 
			messages.info(req, "uncaught Exception")
			return HttpResponseRedirect('/tin/add-individual/')		
		
	else:
		print(form.errors)
		messages.info(req, "invalid form fields")
		return HttpResponseRedirect('/tin/add-individual/')

 


def save_new_individual(req):

	signed_in_user_id = req.session.get("user_id")
	try:		
		
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

		staff_obj = User.objects.get(id = signed_in_user_id)
		office_obj = Office.objects.get(office_name = staff_obj.office.office_name)

		
		check_tin =  AssignedTin.objects.filter(tin = tin)

		if check_tin.exists():
			messages.success(req, "Individual record already created", extra_tags= "record_already_created")
			return HttpResponseRedirect('/tin/add-individual/')
		else:
			tin_obj = AssignedTin.objects.create(tin = tin,  tin_for = "Individuual")
			Individual.objects.create(tin = tin_obj, name = name, gender = gender, date_of_birth = date_of_birth, marital_status = marital_status, state = state, address = address, phone = phone, email = email, occupation = occupation, employment_status = employment_status, work_place= work_place, office = office_obj, staff = staff_obj)
			
			messages.success(req, "User Record Created", extra_tags= "record_created")
			return HttpResponseRedirect('/tin/add-individual/')

		
	except Exception as e:
		print(e)
		return HttpResponseRedirect('/tin/add-individual/')
		 

def c_data_preview(req):

	form = CompanyForm(req.POST)

	if form.is_valid():
		
	
		try:			
			new_tin = generate_tin(req)
			if len(new_tin) == 10:					
				tin_obj = AssignedTin.objects.filter(tin = new_tin)

				while tin_obj.exists():
					new_tin = generate_tin(req)
					tin_obj = AssignedTin.objects.filter(tin = new_tin)

				institution_type = req.POST.get("institution_type")
				institution_category = req.POST.get("institution_category")
				lga = req.POST.get("lga")



				institution = form.cleaned_data.get("institution")
				bussiness_status = form.cleaned_data.get("bussiness_status")
				bussiness_class = form.cleaned_data.get("bussiness_class")
				registration_number = form.cleaned_data.get("registration_number")
				bussiness_ownership_type = form.cleaned_data.get("bussiness_ownership_type")
				bussiness_name = form.cleaned_data.get("bussiness_name")
				bussiness_owner = form.cleaned_data.get("bussiness_owner")
				bussiness_address = form.cleaned_data.get("bussiness_address")
				phone_number = form.cleaned_data.get("phone_number")
				email = form.cleaned_data.get("email")
				employment_status = form.cleaned_data.get("employment_status")
				work_place = form.cleaned_data.get("work_place")

				local_government = LocalGovArea.objects.get(local_government_code = lga)


 
				data_context = {'tin':new_tin, 'lga':local_government.local_government_name, 'institution':institution, 'institution_type':institution_type, 'institution_category':institution_category,   'bussiness_status':bussiness_status, 'bussiness_class':bussiness_class,'registration_number':registration_number, 'bussiness_ownership_type':bussiness_ownership_type, 'bussiness_name':bussiness_name, 'bussiness_owner':bussiness_owner, 'bussiness_address':bussiness_address, 'phone_number':phone_number, 'email':email } 

				
				messages.success(req, "Record Preview",  extra_tags = 'i_data_preview data' )
				return render(req, 'add_company.html', data_context)

			else:
				print("tin cant be generated")	
				return HttpResponseRedirect('/tin/add-company/')
				 		
		except Exception as e:
			print(e)			 
			messages.info(req, "uncaught Exception")
			return HttpResponseRedirect('/tin/add-company/')	

		except User.DoesNotExist:					 
			messages.info(req, "uncaught Exception")
			return HttpResponseRedirect('/tin/add-company/')	

		except Office.DoesNotExist:					 
			messages.info(req, "uncaught Exception")
			return HttpResponseRedirect('/tin/add-company/')		
		
	else:
		print(form.errors)
		messages.info(req, "invalid form fields")
		return HttpResponseRedirect('/tin/add-company/')


def save_new_company(req):

	signed_in_user_id = req.session.get("user_id")
	try:
		lga = req.POST.get("lga")	
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

		staff_obj = User.objects.get(id = signed_in_user_id)
		office_obj = Office.objects.get(office_name = staff_obj.office.office_name)

		 
		institution_type_obj = InstitutionType.objects.get(type_name = institution_type)
		institution_category_obj = InstitutionCategory.objects.get(category_name = institution_category)
		


		 
		 
		check_tin =  AssignedTin.objects.filter(tin = tin)


		if check_tin.exists():

			 
			 
			messages.success(req, "Company record already created", extra_tags= "record_already_created")
			return HttpResponseRedirect('/tin/add-company/')
		else:
			tin_obj = AssignedTin.objects.create(tin = tin,  tin_for = "Company")
			Company.objects.create(tin = tin_obj, local_government = lga, institution = institution, institution_type = institution_type_obj, institution_category = institution_category_obj, bussiness_status = bussiness_status, bussiness_class = bussiness_class,registration_number = registration_number, bussiness_ownership_type = bussiness_ownership_type, bussiness_name = bussiness_name, bussiness_owner = bussiness_owner, bussiness_address = bussiness_address, phone_number = phone_number, email = email, staff = staff_obj, office = office_obj )

			messages.success(req, "User Record Created", extra_tags= "record_created") 
			return HttpResponseRedirect('/tin/add-company/')

		
	except Exception as e:

		print(e)
		return HttpResponseRedirect('/tin/add-company/')

 