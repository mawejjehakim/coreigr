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

def bill_tm(tin, vehicle_type, engine_size, cost_price, chassis, staff, office ):
	existing_office = Office.objects.get(id = office.id)
	existing_staff = User.objects.get(id = staff.id)
	 

			
	# GENERATE BILL

	# Tricycle
	if (engine_size == "Tricycle"):

		try:
			
		 
			#Get particulars [Registration Fee]
			charge_registration_fee = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Registration Fee' )
				
			particulars = "Registration Fee";
			amount = charge_registration_fee.amount or 0
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
						
					
			#Get particulars [New Plate Number]
			charge_new_plate_number = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='New Plate Number' )
				
			particulars = "New Plate Number";
			amount = charge_new_plate_number.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
						
			
			
			
			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_wothiness = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Certificate of road worthiness' )
				
			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_wothiness.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, expiration_date = expirationdate_6months, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			#Get particulars [Vehicle License [Tricycle]]
			charge_vehicle_license = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Vehicle License Tricycle' )
				
			particulars = "Vehicle License [Tricycle]";
			amount = charge_vehicle_license.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, expiration_date = expirationdate_1year, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			
					#Get particulars [Hackney permit]
			charge_hacney_permit = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Hackney permit' )
				
			particulars = "Hackney permit";
			amount = charge_hacney_permit.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, expiration_date = expirationdate_1year, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			
			
			#Get particulars [Driver Badge]
			charge_driver_badge = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Driver Badge' )
				
			particulars = "Driver Badge";
			amount = charge_driver_badge.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, expiration_date = expirationdate_1year, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			return tcode

		except Charge.DoesNotExist:
			messages.info(req, " This type Of charge does Not exist ")
			return HttpResponseRedirect('/tin/add-vehicle/')

		except Exception as e:
			messages.info(req, " UnKnown exception ")
			return HttpResponseRedirect('/tin/add-vehicle/')			
			

	# Motocycle 
	elif engine_size == "Motocycle":

		try:		
			
			#Get particulars [Registration Fee]
			charge_registration_fee = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Registration Fee' )
				
			particulars = "Registration Fee";
			amount = charge_registration_fee.amount or
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
						
			
			#Get particulars [New Plate Number]
			charge_new_plate_number = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='New Plate Number' )
				
			particulars = "New Plate Number";
			amount = charge_new_plate_number.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
						
			
			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_wothiness = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Certificate of road worthiness' )
				
			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_wothiness.amount or 0

			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, expiration_date = expirationdate_1year, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
					
					
			
			
			#Get particulars [Vehicle License [Motocycle]]
			charge_vehicle_license = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Vehicle License Motorcycle' )
				
			particulars = "Vehicle License [Motocycle]";
			amount = charge_vehicle_license.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, expiration_date = expirationdate_1year, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			
			#Get particulars [Hackney permit]
			charge_hacney_permit = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Hackney permit' )
				
			particulars = "Hackney permit";
			amount = charge_hacney_permit.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, expiration_date = expirationdate_1year, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			
			
			#Get particulars [Driver Badge]
			charge_driver_badge = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Driver Badge' )
				
			particulars = "Driver Badge";
			amount = charge_driver_badge.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, expiration_date = expirationdate_1year, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			


#Get particulars [SMS Alert]
			charge_sms_alert = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='SMS Alert' )
				
			particulars = "SMS Alert";
			amount = charge_sms_alert.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
						
			
			
			#Get particulars [Stamp Duty]
			charge_stamp_duty = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Stamp Duty' )
				
			particulars = "Stamp Duty";
			amount = charge_stamp_duty.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			return tcode

		except Charge.DoesNotExist:
			messages.info(req, " This type Of charge does Not exist ")
			return HttpResponseRedirect('/tin/add-vehicle/')

		except Exception as e:
			messages.info(req, " UnKnown exception ")
			return HttpResponseRedirect('/tin/add-vehicle/')		
