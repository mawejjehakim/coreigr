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

def bill_ppb(tin, vehicle_type, engine_size, cost_price, chassis, staff, office ):
	existing_office = Office.objects.get(id = office.id)
	existing_staff = User.objects.get(id = staff.id)
 

# GENERATE BILL

# 1.6 - 2.0   -  Above 1 million
	if (engine_size == "1.6 - 2.0" and cost_price =="Price of vehicle above 1 million"):

		try:
			
		
			#Get particulars [Registration Book]
			charge_registration_book = Charge.objects.get(options='New', vehicle_type='Private Pickup/Bus', particular='Registration Book')
				
			particulars = "Registration Book";
			amount = charge_registration_book.amount or 0
			
	 
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			#Get particulars [Inspection Fee]
			charge_inspection_fee = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Inspection Fee')
				
			particulars = "Inspection Fee";
			amount = charge_inspection_fee.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Proof of ownership]
			charge_proof_of_ownership = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Proof of ownership')
				
			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			#Get particulars [New Plate Number]
			charge_new_plate_number = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='New Plate Number')
				
			particulars = "New Plate Number";
			amount = charge_new_plate_number.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Price of vehicle above 1 million]
			charge_price_above_1m = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Price of vehicle above 1 million')
				
			particulars = "Registration for Price of vehicle above 1 million";
			amount = charge_price_above_1m.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_road_worthness = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Certificate of road worthiness')
				
			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_road_worthness.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			#Get particulars [Vehicle License [1.6 - 2.0]]
			charge_vehicle_lincense = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Vehicle License [1.6 - 2.0]')
				
			particulars = "Vehicle License [1.6 - 2.0]";
			amount = charge_vehicle_lincense.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			



	# 2.1 - 3.0   -  Above 1 million
	elif (engine_size == "2.1 - 3.0" and cost_price =="Price of vehicle above 1 million"):
		
			#Get particulars [Registration Book]
			charge_registration_book = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Registration Book')
				
			particulars = "Registration Book";
			amount = charge_registration_book.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Inspection Fee]
			charge_inspection_fee = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Inspection Fee')
				
			particulars = "Inspection Fee";
			amount = charge_inspection_fee.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Proof of ownership]
			charge_proof_of_ownership = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Proof of ownership')
				
			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			#Get particulars [New Plate Number]
			charge_new_plate_number = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='New Plate Number')
				
			particulars = "New Plate Number";
			amount = charge_new_plate_number.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Price of vehicle above 1 million]
			charge_price_above_1m = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Price of vehicle above 1 million')
				
			particulars = "Registration for Price of vehicle above 1 million";
			amount = charge_price_above_1m.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_worthiness = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Certificate of road worthiness')
				
			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_worthiness.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			#Get particulars [Vehicle License [2.1 - 3.0]]
			charge_registration_book = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Vehicle License [2.1 - 3.0]')
				
			particulars = "Vehicle License [2.1 - 3.0]";
			amount = charge_.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			



	# 3.1 - Above   -  Above 1 million
	elif (engine_size == "3.1 - Above" and cost_price =="Price of vehicle above 1 million"):
		
			#Get particulars [Registration Book]
			charge_registration_book = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Registration Book')
				
			particulars = "Registration Book";
			amount = charge_.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Inspection Fee]
			charge_inspection_fee = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Inspection Fee')
				
			particulars = "Inspection Fee";
			amount = charge_inspection_fee.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Proof of ownership]
			charge_proof_of_ownership = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Proof of ownership')
				
			particulars = "Proof of ownership";
			amount = charge_.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			#Get particulars [New Plate Number]
			charge_new_plate_number = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='New Plate Number')
				
			particulars = "New Plate Number";
			amount = charge_new_plate_number.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Price of vehicle above 1 million]
			charge_price_above_1m = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Price of vehicle above 1 million')
				
			particulars = "Registration for Price of vehicle above 1 million";
			amount = charge_price_above_1m.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_worthiness = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Certificate of road worthiness')
				
			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_worthiness.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			#Get particulars [Vehicle License [3.1 - above]]
			charge_vehicle_lincense = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Vehicle License [3.1 - above]')
				
			particulars = "Vehicle License [3.1 - above]";
			amount = charge_vehicle_lincense.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			




	#=======================================================================================================================================================
	# 1.6 - 2.0   -  Price of vehicle below 1 million
	elif (engine_size == "1.6 - 2.0" and cost_price =="Price of vehicle below 1 million"):
		
			#Get particulars [Registration Book]
			charge_registration_book = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Registration Book')
				
			particulars = "Registration Book";
			amount = charge_charge_registration_book.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Inspection Fee]
			charge_inspection_fee = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Inspection Fee')
				
			particulars = "Inspection Fee";
			amount = charge_inspection_fee.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Proof of ownership]
			charge_proof_of_ownership = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Proof of ownership')
				
			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			#Get particulars [New Plate Number]
			charge_new_plate_number = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='New Plate Number')
				
			particulars = "New Plate Number";
			amount = charge_new_plate_number.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Price of vehicle below 1 million]
			charge_price_below_im = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Price of vehicle below 1 million')
				
			particulars = "Registration for Price of vehicle below 1 million";
			amount = charge_price_below_im.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_worthiness = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Certificate of road worthiness')
				
			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_worthiness.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			#Get particulars [Vehicle License [1.6 - 2.0]]
			charge_vehicle_lincense = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Vehicle License [1.6 - 2.0]')
				
			particulars = "Vehicle License [1.6 - 2.0]";
			amount = charge_vehicle_lincense.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			



	# 2.1 - 3.0   -  Price of vehicle below 1 million
	elif (engine_size == "2.1 - 3.0" and cost_price =="Price of vehicle below 1 million"):
		
			#Get particulars [Registration Book]
			charge_registration_book = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Registration Book')
				
			particulars = "Registration Book";
			amount = charge_registration_book.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Inspection Fee]
			charge_inspection_fee = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Inspection Fee')
				
			particulars = "Inspection Fee";
			amount = charge_inspection_fee.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Proof of ownership]
			charge_proof_of_ownership = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Proof of ownership')
				
			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			#Get particulars [New Plate Number]
			charge_new_plate_number = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='New Plate Number')
				
			particulars = "New Plate Number";
			amount = charge_new_plate_number.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Price of vehicle below 1 million]
			charge_price_above_1m = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Price of vehicle below 1 million')
				
			particulars = "Registration for Price of vehicle below 1 million";
			amount = charge_price_above_1m.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_road_worthness = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Certificate of road worthiness')
				
			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_road_worthness.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			#Get particulars [Vehicle License [2.1 - 3.0]]
			charge_vehicle_lincense = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Vehicle License [2.1 - 3.0]')
				
			particulars = "Vehicle License [2.1 - 3.0]";
			amount = charge_vehicle_lincense.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			



	# 3.1 - Above   -  Price of vehicle below 1 million
	elif (engine_size == "3.1 - Above" and cost_price =="Price of vehicle below 1 million"):
		
			#Get particulars [Registration Book]
			charge_registration_book = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Registration Book')
				
			particulars = "Registration Book";
			amount = charge_registration_book.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Inspection Fee]
			charge_inspection_fee = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Inspection Fee')
				
			particulars = "Inspection Fee";
			amount = charge_inspection_fee.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Proof of ownership]
			charge_proof_of_ownership = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Proof of ownership')
				
			particulars = "Proof of ownership";
			amount = charge_charge_proof_of_ownership.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
			
			
			#Get particulars [New Plate Number]
			charge_new_plate_number = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='New Plate Number')
				
			particulars = "New Plate Number";
			amount = charge_charge_proof_of_ownership.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
			
			#Get particulars [Price of vehicle below 1 million]
			charge_price_above_1m = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Price of vehicle below 1 million')
				
			particulars = "Registration for Price of vehicle below 1 million";
			amount = charge_price_above_1m.amount or 0
			
			
			TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

			
		
		#Get particulars [Certificate of road worthiness]
	charge_certificate_of_road_worthness = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Certificate of road worthiness')
		
	particulars = "Certificate of road worthiness";
	amount = charge_certificate_of_road_worthness.amount or 0
	
	
	TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
	
	
	#Get particulars [Vehicle License [3.1 - above]]
	charge_vehicle_lincense = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Vehicle License [3.1 - above]')
		
	particulars = "Vehicle License [3.1 - above]";
	amount = charge_vehicle_lincense.amount or 0
	
	
	TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis,expiration_date = expirationdate_1year, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)
	
	




#Get particulars [SMS Alert]
	charge_sms_alert = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='SMS Alert')
		
	particulars = "SMS Alert";
	amount = charge_sms_alert.amount or 0
	
	
	TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

	
	
	
	#Get particulars [Stamp Duty]
	charge_stamp_duty = Charge.objects.get(options='New',vehicle_type='Private Pickup/Bus', particular='Stamp Duty')
		
	particulars = "Stamp Duty";
	amount = charge_stamp_duty.amount or 0
	
	
	TransactionAssessment.objects.create(transaction_code = tcode, tin = existing_tin, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", payment_status = "Not Paid", transaction_staff = existing_staff, transaction_office = existing_office)

