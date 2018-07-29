from django.shortcuts import render
from coreIGR_app.forms import MDAForm
from coreIGR_app.models import MDA

from django.http import HttpResponseRedirect

from django.contrib import messages

def add_new_mda(req):

	form = MDAForm(req.POST)

	if form.is_valid():
	
		try:
			mda_name = form.cleaned_data.get("mda_name")
			
			lga_obj, created =  MDA.objects.get_or_create(mda_name = mda_name)

			if created:		

				messages.success(req, "MDA Created")
				return HttpResponseRedirect('/mda/add-mda/')

			else:				 
				messages.success(req, "MDA already exist")
				return HttpResponseRedirect('/mda/add-mda/')

		except Exception as e:			 
			messages.info(req, "uncaught Exception")
			return HttpResponseRedirect('/mda/add-mda/')	
		
	else:
		messages.info(req, "invalid form fields")
		return HttpResponseRedirect('/mda/add-mda/')

def get_genearate_bill(req):
 

	form = TINForm(req.POST)

	if form.is_valid():
	
		try:
			tin = form.cleaned_data.get("tin_number")
			
			individual_obj = Individual.objects.get(tin = tin)
			tin =  individual_obj.name
			phone = individual_obj.phone
			email = individual_obj.email

			

			header("Location: create_bill.php");




			 
		except Individual.DoesnotExist:	

			try:
				company_obj = Company.objects.get(tin = tin)
				tin  = tin	
				name = company_obj.bussiness_name
				phone = company_obj.phone
				email = company_obj.email

				header("Location: create_bill.php");

				

			except Company.DoesnotExist as e:
					print(e)			
					return HttpResponseRedirect('/mda/generate-bill/')

		except Exception as e:			 
			messages.info(req, "uncaught Exception")
			return HttpResponseRedirect('/mda/generate-bill/')	
		
	else:
		messages.info(req, "invalid form fields")
		return HttpResponseRedirect('/mda/generate-bill/')


 
