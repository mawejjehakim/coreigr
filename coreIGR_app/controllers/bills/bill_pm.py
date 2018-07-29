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
expirationdate_6months = today + relativedelta(month=6)

 
		
# GENERATE BILL

def bill_pm(tin, vehicle_type, engine_size, cost_price, chassis, staff, office ):
	existing_office = Office.objects.get(id = office.id)
	existing_staff = User.objects.get(id = staff.id)
	
	 
		
# GENERATE BILL


		
		#Get particulars [Registration Fee]
	charge_registration_fee =  Charge.objects.filter(options='New', vehicle_type='Private Motorcycle', particulars='Registration Fee')[0]
		
	particulars = "Registration Fee";
	amount = charge_registration_fee.amount or 0		
	
	
	
	#Get particulars [New Plate Number]
	charge_new_plate_number =  Charge.objects.filter(options='New', vehicle_type='Private Motorcycle', particulars='New Plate Number')[0]
		
	particulars = "New Plate Number";
	amount = charge_new_plate_number.amount or 0
	
	
	TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
	
	#Get particulars [Certificate of road worthiness]
	charge_certificate_of_road_worthness =  Charge.objects.filter(options='New', vehicle_type='Private Motorcycle', particulars='Certificate of road worthiness')[0]
		
	particulars = "Certificate of road worthiness";
	amount = charge_certificate_of_road_worthness.amount or 0
	
	
	TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, expiration_date = expirationdate_1year, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
	
	
	#Get particulars [Vehicle License [Motocycle]]
	charge_vehicle_lincense =  Charge.objects.filter(options='New', vehicle_type='Private Motorcycle', particulars='Vehicle License Motorcycle')[0]
		
	particulars = "Vehicle License [Motocycle]";
	amount =charge_vehicle_lincense.amount or 0
	
	
	TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, expiration_date = expirationdate_1year, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
	
	
					#Get particulars [Hackney permit]
	charge_hackney_permit =  Charge.objects.filter(options='New', vehicle_type='Private Motorcycle', particulars='Hackney permit')[0]
		
	particulars = "Hackney permit";
	amount = charge_hackney_permit.amount or 0
	
	
	TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, expiration_date = expirationdate_1year, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
	
	
	
	#Get particulars [Driver Badge]
	charge_driver_badge  = Charge.objects.filter(options='New', vehicle_type='Private Motorcycle', particulars='Driver Badge')[0]
		
	particulars = "Driver Badge";
	amount = charge_driver_badge.amount or 0
	
	
	TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, expiration_date = expirationdate_1year, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
	
	
	
			

#Get particulars [SMS Alert]
	charge_sms_alert =  Charge.objects.filter(options='New', vehicle_type='Private Motorcycle', particulars='SMS Alert')[0]
		
	particulars = "SMS Alert";
	amount = charge_sms_alert.amount or 0
	
	
	TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
	
	
	#Get particulars [Stamp Duty]
	Charge.objects.filter(options='New', vehicle_type='Private Motorcycle', particulars='Stamp Duty')[0]
		
	particulars = "Stamp Duty";
	amount = row['amount'];
	
	
	TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
