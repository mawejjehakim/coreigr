from django.shortcuts import render
from django.contrib import messages
from coreIGR_app.models import User, Office, NumberPlate, LocalGovArea, AssignedNumberPlate
from coreIGR_app.forms import PlateNumberForm

from django.http import HttpResponseRedirect


def p_n_data_preview(req):

	signed_in_user_id = req.session.get("user_id")

	form = PlateNumberForm(req.POST)

	if form.is_valid():


		local_government = req.POST.get('local_government')
		number_plate = form.cleaned_data.get("number_plate")
		

		try:			
			office = NumberPlate.objects.get(number_plate = number_plate)		

			messages.success(req, " Record Preview ",  extra_tags = 'plate_exist' )
			return render(req, 'add_number_plate.html')
	 	

		except NumberPlate.DoesNotExist:

			data_context = {'local_government':local_government, 'number_plate':number_plate, }
			messages.success(req, " Record Preview ",  extra_tags = 'n_p_data_preview' )
			return render(req, 'add_number_plate.html', data_context)

		
		except Exception as e:					 
			messages.info(req, "Un Caught Exception")
			return HttpResponseRedirect('/store/add-number-plate/')		
		
	else:
		print(form.errors)
		messages.info(req, "invalid form fields")
		return HttpResponseRedirect('/store/add-number-plate/')


def save_new_plate_number(req):
	signed_in_user_id = req.session.get("user_id")		 

	number_plate = req.POST.get("number_plate")
	local_government = req.POST.get("local_government")

	staff_obj = User.objects.get(id = signed_in_user_id) 

	try:
		
		NumberPlate.objects.create(local_government = local_government, number_plate = number_plate, staff = staff_obj )
		messages.success(req, "NumberPlate Record Created", extra_tags= "record_created")
		return HttpResponseRedirect('/store/add-number-plate/')
		
	except Exception as e:
		messages.success(req, "NumberPlate Already Created", extra_tags= "record_already_exist")
		return HttpResponseRedirect('/store/add-number-plate/')
	 
	
	



def get_localgov_numberplates(req):


	LGAs = LocalGovArea.objects.all()
	lga = req.POST.get("lga")
	office_name = req.POST.get("office_name")
	req.session['sess_office_name'] = office_name

		 
	req.session['sess_lga'] = lga	 

	try:	 
		office_obj = Office.objects.get(office_name = office_name)		  

		number_plates = NumberPlate.objects.filter(local_government = lga, is_issued=False)

		issued_number_plates = AssignedNumberPlate.objects.filter( office = office_obj.id)
		req.session['sess_office_id'] = office_obj.id

		return render(req, 'assign_plate_number.html', {"LGAs":LGAs,'number_plates':number_plates,'lg':lga, 'issued_number_plates':issued_number_plates, 'office_name':office_obj.office_name})
	except Exception as e:
		print(e)

 

	 









	
	 

	 