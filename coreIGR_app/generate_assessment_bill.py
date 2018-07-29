from coreIGR_app.controllers.bills.bill_ps import bill_ps 
from coreIGR_app.controllers.bills.bill_cvs import bill_cvs
from coreIGR_app.controllers.bills.bill_ppb import bill_ppb
from coreIGR_app.controllers.bills.bill_dv import bill_dv
from coreIGR_app.controllers.bills.bill_ct import bill_ct
from coreIGR_app.controllers.bills.bill_tm import bill_tm
from coreIGR_app.controllers.bills.bill_pm import bill_pm
from coreIGR_app.controllers.bills.bill_dtm import bill_dtm



def generate_assessment_bill(tin, vehicle_type, engine_size, cost_price, chassis, staff, office):


	if vehicle_type == "Private Vehicle Saloon":
		return bill_ps(tin, vehicle_type, engine_size, cost_price, chassis, staff, office)
		
	elif vehicle_type == "Commercial Vehicle Saloon":
		bill_cvs(tin, vehicle_type, engine_size, cost_price, chassis, staff, office)
		
	elif vehicle_type == "Private Pickup/Bus":
		bill_ppb(tin, vehicle_type, engine_size, cost_price, chassis, staff, office)
		
	elif vehicle_type == "Commercial Pickup/Bus":
		bill_cpb(tin, vehicle_type, engine_size, cost_price, chassis, staff, office)
		
	elif vehicle_type == "Dealers Vehicle":
		bill_dv(tin, vehicle_type, engine_size, cost_price, chassis, staff, office)
		
	elif vehicle_type == "Commercial Truck/Trailer/Lorry/Tipper":
		bill_ct(tin, vehicle_type, engine_size, cost_price, chassis, staff, office)
		
	elif vehicle_type == "Commercial Tricycle/Motorcycle":
		bill_tm(tin, vehicle_type, engine_size, cost_price, chassis, staff, office)
		
	elif vehicle_type == "Private Motorcycle":
		bill_pm(tin, vehicle_type, engine_size, cost_price, chassis, staff, office)
	
	elif vehicle_type == "Dealers Tricycle/Motorcycle":
		bill_dtm(tin, vehicle_type, engine_size, cost_price, chassis, staff, office)
	


# _SESSION['xtcode'] = tcode;
# _SESSION['assessment_chassis'] = chassis;
 