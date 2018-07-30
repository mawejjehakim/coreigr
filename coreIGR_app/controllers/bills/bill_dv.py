from random import randint
from dateutil.relativedelta import relativedelta
from datetime import date

from django.contrib import messages
from django.http import HttpResponseRedirect


from coreIGR_app.models import Charge, TransactionAssessment, AssignedTin, Office, User
#  pip install python-dateutil install 
range_start = 10**(8-1)
range_end = (10**8)-1
generated_rand_num =  randint(range_start, range_end)
tcode = "ML"+str(generated_rand_num)


today = date.today()
expirationdate_1year = today + relativedelta(years=1) 

 
		
# GENERATE BILL

def bill_dv(req, existing_tin, vehicle_type, engine_size, cost_price, chassis, staff, office ):

	existing_office = Office.objects.get(id = office.id)
	existing_staff = User.objects.get(id = staff.id) 

	tin_obj = AssignedTin.objects.get(tin = existing_tin)
 
	
	# Get particulars [Registration Fee]

	try:
		charge_registration_fee =  Charge.objects.get(options='New', vehicle_type='Dealers Vehicle', particulars='Registration Fee' )

		particulars = "Registration Fee";
		amount = charge_registration_fee.amount or 0


		TransactionAssessment.objects.create(transaction_code = tcode, tin = tin_obj, expiration_date = expirationdate_1year,  chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
	

		# Get particulars [SMS Alert]
		charge_sms_alert = Charge.objects.get(options='New', vehicle_type='Dealers Vehicle', particulars='SMS Alert' )
			
		particulars = "SMS Alert";
		amount = charge_sms_alert.amount or 0	
		
		TransactionAssessment.objects.create(transaction_code = tcode, tin = tin_obj, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)		
		
		
		# Get particulars [Stamp Duty]

		charge_stamp_duty = Charge.objects.get(options ='New', vehicle_type='Dealers Vehicle', particulars='Stamp Duty' )
			
		particulars = "Stamp Duty";
		amount = charge_stamp_duty.amount or 0

		# print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx           " + tcode)

		TransactionAssessment.objects.create(transaction_code = tcode, tin = tin_obj, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)		

		req.session["correct_charge"] = "yes"

		print(tcode) 
		return tcode



		

	except Charge.DoesNotExist as e:
		messages.success(req, "Vehicle Record Created", extra_tags= "charge_unavailable")
		# return HttpResponseRedirect('/mla/get-tin-info/')
	except Exception as e:
		raise e
		print(e) 