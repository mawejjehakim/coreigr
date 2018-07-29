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

def bill_ct(tin, vehicle_type, engine_size, cost_price, chassis, staff, office ):
	existing_office = Office.objects.get(id = office.id)
	existing_staff = User.objects.get(id = staff.id)
	 

 
	
		
# GENERATE BILL

# 6 - 8 tyres   -  Above 1 million
	if (engine_size == "6 - 8 tyres"):
		
			#Get particulars [Registration Fee]
			charge_registration_fee =  Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Registration Fee')
				
			particulars = "Registration Fee";
			amount = charge_registration_fee.amount or 0
			

			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)		
			
			
			 #Get particulars [Registration Book]
			charge_registration_book =Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Registration Book')
				
			particulars = "Registration Book";
			amount = charge_registration_book.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)		
			
			
			#Get particulars [Inspection Fee]
			charge_inspection_fee = Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Inspection Fee')
				
			particulars = "Inspection Fee";
			amount = charge_inspection_fee.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)		
			
			
			#Get particulars [Proof of ownership]
			charge_proof_of_ownership = Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Proof of ownership')
				
			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			#Get particulars [New Plate Number]
			charge_new_plate_number = Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='New Plate Number')
				
			particulars = "New Plate Number";
			amount = charge_new_plate_number.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)		
			
			
			
			
			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_wothiness = Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Certificate of road worthiness')
				
			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_wothiness.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, expiration_date = expirationdate_6months, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)	
			#Get particulars [Vehicle License [6 - 8 tyres]]
			
			charge_vehicle_license =  Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Vehicle License [6 - 8 tyres]')
				
			particulars = "Vehicle License [6 - 8 tyres]";
			amount = charge_vehicle_license.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
					#Get particulars [Hackney permit]
			charge_hacney_permit = Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Hackney permit [6 - 8 tyres]')
				
			particulars = "Hackney permit";
			amount = charge_hacney_permit.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			
			#Get particulars [Driver Badge]
			charge_driver_badge  = Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Driver Badge')
				
			particulars = "Driver Badge";
			amount = charge_driver_badge.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			
					#Get particulars [Conductors Badge]
			charge_conductor_badge = Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Conductors Badge')
				
			particulars = "Conductors Badge";
			amount = charge_conductor_badge.amount
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			



	# 10 tyres - above 
	elif (engine_size == "10 tyres - above"):
		
			#Get particulars [Registration Fee]
			charge_registration_fee =  Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Registration Fee')
				
			particulars = "Registration Fee";
			amount = charge_registration_fee.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)		
			
			
			#Get particulars [Registration Book]
			charge_registration_book = Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Registration Book')
				
			particulars = "Registration Book";
			amount = charge_registration_book.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)		
			
			
			#Get particulars [Inspection Fee]
			charge_inspection_fee = Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Inspection Fee')
				
			particulars = "Inspection Fee";
			amount = charge_inspection_fee.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)		
			
			
			#Get particulars [Proof of ownership]
			charge_proof_of_ownership = Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Proof of ownership')
				
			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			#Get particulars [New Plate Number]
			charge_new_plate_number =Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='New Plate Number')
				
			particulars = "New Plate Number";
			amount = charge_new_plate_number.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)		
			
			
			
			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_wothiness = Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Certificate of road worthiness')
				
			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_wothiness.amount or 0
			
			
			
			
			#Get particulars [Vehicle License [10 tyres - above]]
			charge_vehicle_license =  Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Vehicle License [10 tyres - above]')
				
			particulars = "Vehicle License [10 tyres - above]";
			amount = charge_vehicle_license.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			# xxx
			
							#Get particulars [Hackney permit]
			charge_hacney_permit = Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Hackney permit [10 tyres - above]')
				
			particulars = "Hackney permit";
			amount = charge_hacney_permit.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			
			#Get particulars [Driver Badge]
			charge_driver_badge = Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Driver Badge')
				
			particulars = "Driver Badge";
			amount = charge_driver_badge.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			
					#Get particulars [Conductors Badge]
			charge_conductor_badge = Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Conductors Badge')
				
			particulars = "Conductors Badge";
			amount = charge_conductor_badge.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			return tcode

		except Charge.DoesNotExist:
			messages.info(req, "This Type of Charge does not exist ")
			return HttpResponseRedirect('/tin/add-vehicle/')
		
		except Exception as e:
			messages.info(req, " UnKnown exception ")
			return HttpResponseRedirect('/tin/add-vehicle/') 


#Get particulars [SMS Alert]
	charge_sms_alert =  Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='SMS Alert')
		
	particulars = "SMS Alert";
	amount = charge_sms_alert.amount or 0
	
	
	TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)		
	
	
	
	#Get particulars [Stamp Duty]
	charge_stamp_duty = Charge.objects.get(options='New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Stamp Duty')
		
	particulars = "Stamp Duty";
	amount = charge_stamp_duty.amount or 0
	
	
	TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)		
	
 