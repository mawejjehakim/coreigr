from random import randint
from dateutil.relativedelta import relativedelta
from datetime import date

from coreIGR_app.models import Charge, TransactionAssessment, AssignedTin, Office, User
#  pip install python-dateutil install 
range_start = 10**(8-1)
range_end = (10**8)-1
generated_rand_num =  randint(range_start, range_end)
tcode = "ML"+str(generated_rand_num)


today = date.today()
expirationdate_1year = today + relativedelta(years=1) 
 
		
# GENERATE BILL

def bill_dtm(tin, vehicle_type, engine_size, cost_price, chassis, staff, office ):
	existing_office = Office.objects.get(id = office.id)
	existing_staff = User.objects.get(id = staff.id)
	 
	
		
# GENERATE BILL
	try:
	
	#Get particulars [Registration Fee]
		charge_registration_fee = Charge.objects.get(options='New',  vehicle_type='Dealers Tricycle/Motocycle',  particulars='Registration Fee' )
			
		particulars = "Registration Fee";
		amount =charge_registration_fee.amount or 0

		TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, expiration_date =expirationdate_6months, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)


		#Get particulars [SMS Alert]
		charge_sms_alert = Charge.objects.get(options='New',  vehicle_type='Dealers Tricycle/Motocycle',  particulars='SMS Alert' )
			
		particulars = "SMS Alert";
		amount = charge_sms_alert.amount or 0

		TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)



		#Get particulars [Stamp Duty]
		charge_stamp_duty = Charge.objects.get(options ='New',  vehicle_type='Dealers Tricycle/Motocycle',  particulars='Stamp Duty' )
			
		particulars = "Stamp Duty";
		amount =charge_stamp_duty.amount or 0

		TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

		return tcode
	except Charge.DoesNotExist:
		messages.info(req, "This Type of Charge does not exist ")
		return HttpResponseRedirect('/tin/add-vehicle/')

	except Exception as e:
		messages.info(req, " UnKnown exception ")
		return HttpResponseRedirect('/tin/add-vehicle/')
	
	 

