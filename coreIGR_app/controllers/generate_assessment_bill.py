from coreIGR_app.controllers.bills.bill_ps import bill_ps 
from coreIGR_app.controllers.bills.bill_cvs import bill_cvs
from coreIGR_app.controllers.bills.bill_ppb import bill_ppb
from coreIGR_app.controllers.bills.bill_dv import bill_dv
from coreIGR_app.controllers.bills.bill_ct import bill_ct
from coreIGR_app.controllers.bills.bill_tm import bill_tm
from coreIGR_app.controllers.bills.bill_pm import bill_pm
from coreIGR_app.controllers.bills.bill_dtm import bill_dtm
from coreIGR_app.controllers.bills.bill_cpb import bill_cpb


def generate_assessment_bill(req, tin, vehicle_category, engine_size, cost_price, chassis_number, staff, office):


	tin = tin
	vehicle_category = vehicle_category
	engine_size = engine_size
	cost_price = cost_price
	chassis = chassis_number

	staff = staff
	office = office

	if vehicle_category == "Private Vehicle Saloon":
		return bill_ps(req, tin, vehicle_category, engine_size, cost_price, chassis_number, staff, office)
		
	elif vehicle_category == "Commercial Vehicle Saloon":
		return bill_cvs(req, tin, vehicle_category, engine_size, cost_price, chassis_number, staff, office)
		
	elif vehicle_category == "Private Pickup/Bus":
		return bill_ppb(req, tin, vehicle_category, engine_size, cost_price, chassis_number, staff, office)
		
	elif vehicle_category == "Commercial Pickup/Bus":
		return bill_cpb(req, tin, vehicle_category, engine_size, cost_price, chassis_number, staff, office)
		
	elif vehicle_category == "Dealers Vehicle":
		return bill_dv(req, tin, vehicle_category, engine_size, cost_price, chassis_number, staff, office)
		
	elif vehicle_category == "Commercial Truck/Trailer/Lorry/Tipper":
		return bill_ct(req, tin, vehicle_category, engine_size, cost_price, chassis_number, staff, office)
		
	elif vehicle_category == "Commercial Tricycle/Motorcycle":
		return bill_tm(req, tin, vehicle_category, engine_size, cost_price, chassis_number, staff, office)
		
	elif vehicle_category == "Private Motorcycle":
		return bill_pm(req, tin, vehicle_category, engine_size, cost_price, chassis_number, staff, office)
	
	elif vehicle_category == "Dealers Tricycle/Motorcycle":
		return bill_dtm(req, tin, vehicle_category, engine_size, cost_price, chassis_number, staff, office)
	


# _SESSION['xtcode'] = tcode;
# _SESSION['assessment_chassis'] = chassis;
 