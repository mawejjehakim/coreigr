<?php
	//Generate Expiration Dates 1 year
	$tdate = date("Y/m/d");
	$issuedate = date("Y/m/d");
	$y = date("Y") + 1;
	$m = date("m");
	$d = date("d");
	$expirationdate_1year = $y."/".$m."/".$d;
	
	
	//Generate Expiration Dates 6 months

	$mm = date("m");
	$dd = date("d");
	
	if ($mm == "01"){
		$six_month = "07";
		$yy = date("Y");
	}elseif($mm == "02"){
		$six_month = "08";
		$yy = date("Y");
	}elseif($mm == "03"){
		$six_month = "09";
		$yy = date("Y");
	}elseif($mm == "04"){
		$six_month = "10";
		$yy = date("Y"); 	
	}elseif($mm == "05"){
		$six_month = "11";
		$yy = date("Y");	
	}elseif($mm == "06"){
		$six_month = "12";	
		$yy = date("Y");
	}elseif($mm == "07"){
		$six_month = "01";
		$yy = date("Y") + 1;	
	}elseif($mm == "08"){
		$six_month = "02";
		$yy = date("Y") + 1; 	
	}elseif($mm == "09"){
		$six_month = "03"; 
		$yy = date("Y") + 1;	
	}elseif($mm == "10"){
		$six_month = "04";	
		$yy = date("Y") + 1;
	}elseif($mm == "11"){
		$six_month = "05";	
		$yy = date("Y") + 1;
	}elseif($mm == "12"){
		$six_month = "06";	
		$yy = date("Y") + 1;
	}
	$expirationdate_6months = $yy."/".$six_month."/".$dd;
	
		
// GENERATE BILL

// 1.6 - 2.0   -  Above 1 million
if ($engine_size == "1.6 - 2.0" && $cost_price =="Price of vehicle above 1 million"){
	
		//Get particulars [Registration Book]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Registration Book'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Registration Book";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Inspection Fee]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Inspection Fee'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Inspection Fee";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Proof of ownership]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Proof of ownership'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Proof of ownership";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [New Plate Number]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='New Plate Number'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "New Plate Number";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Price of vehicle above 1 million]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Price of vehicle above 1 million'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Registration for Price of vehicle above 1 million";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Certificate of road worthiness]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Certificate of road worthiness'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Certificate of road worthiness";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_6months','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Vehicle License [1.6 - 2.0]]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Vehicle License [1.6 - 2.0]'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Vehicle License [1.6 - 2.0]";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
				//Get particulars [Hackney permit]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Hackney permit'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Hackney permit";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
		//Get particulars [Driver Badge]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Driver Badge'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Driver Badge";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
				//Get particulars [Conductors Badge]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Conductors Badge'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Conductors Badge";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
}


// 2.1 - 3.0   -  Above 1 million
if ($engine_size == "2.1 - 3.0" && $cost_price =="Price of vehicle above 1 million"){
	
		//Get particulars [Registration Book]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Registration Book'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Registration Book";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Inspection Fee]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Inspection Fee'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Inspection Fee";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Proof of ownership]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Proof of ownership'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Proof of ownership";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [New Plate Number]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='New Plate Number'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "New Plate Number";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Price of vehicle above 1 million]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Price of vehicle above 1 million'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Registration for Price of vehicle above 1 million";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Certificate of road worthiness]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Certificate of road worthiness'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Certificate of road worthiness";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_6months','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Vehicle License [2.1 - 3.0]]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Vehicle License [2.1 - 3.0]'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Vehicle License [2.1 - 3.0]";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
						//Get particulars [Hackney permit]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Hackney permit'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Hackney permit";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
		//Get particulars [Driver Badge]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Driver Badge'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Driver Badge";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
				//Get particulars [Conductors Badge]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Conductors Badge'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Conductors Badge";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
}


// 3.1 - Above   -  Above 1 million
if ($engine_size == "3.1 - Above" && $cost_price =="Price of vehicle above 1 million"){
	
		//Get particulars [Registration Book]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Registration Book'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Registration Book";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Inspection Fee]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Inspection Fee'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Inspection Fee";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Proof of ownership]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Proof of ownership'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Proof of ownership";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [New Plate Number]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='New Plate Number'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "New Plate Number";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Price of vehicle above 1 million]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Price of vehicle above 1 million'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Registration for Price of vehicle above 1 million";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Certificate of road worthiness]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Certificate of road worthiness'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Certificate of road worthiness";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_6months','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Vehicle License [3.1 - above]]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Vehicle License [3.1 - above]'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Vehicle License [3.1 - above]";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
						//Get particulars [Hackney permit]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Hackney permit'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Hackney permit";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
		//Get particulars [Driver Badge]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Driver Badge'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Driver Badge";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
				//Get particulars [Conductors Badge]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Conductors Badge'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Conductors Badge";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
}



//=======================================================================================================================================================
// 1.6 - 2.0   -  Price of vehicle below 1 million
if ($engine_size == "1.6 - 2.0" && $cost_price =="Price of vehicle below 1 million"){
	
		//Get particulars [Registration Book]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Registration Book'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Registration Book";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Inspection Fee]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Inspection Fee'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Inspection Fee";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Proof of ownership]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Proof of ownership'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Proof of ownership";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [New Plate Number]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='New Plate Number'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "New Plate Number";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Price of vehicle below 1 million]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Price of vehicle below 1 million'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Registration for Price of vehicle below 1 million";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Certificate of road worthiness]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Certificate of road worthiness'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Certificate of road worthiness";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_6months','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Vehicle License [1.6 - 2.0]]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Vehicle License [1.6 - 2.0]'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Vehicle License [1.6 - 2.0]";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
						//Get particulars [Hackney permit]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Hackney permit'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Hackney permit";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
		//Get particulars [Driver Badge]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Driver Badge'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Driver Badge";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
				//Get particulars [Conductors Badge]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Conductors Badge'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Conductors Badge";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
}


// 2.1 - 3.0   -  Price of vehicle below 1 million
if ($engine_size == "2.1 - 3.0" && $cost_price =="Price of vehicle below 1 million"){
	
		//Get particulars [Registration Book]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Registration Book'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Registration Book";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Inspection Fee]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Inspection Fee'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Inspection Fee";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Proof of ownership]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Proof of ownership'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Proof of ownership";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [New Plate Number]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='New Plate Number'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "New Plate Number";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Price of vehicle below 1 million]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Price of vehicle below 1 million'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Registration for Price of vehicle below 1 million";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Certificate of road worthiness]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Certificate of road worthiness'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Certificate of road worthiness";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_6months','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Vehicle License [2.1 - 3.0]]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Vehicle License [2.1 - 3.0]'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Vehicle License [2.1 - 3.0]";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
						//Get particulars [Hackney permit]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Hackney permit'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Hackney permit";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
		//Get particulars [Driver Badge]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Driver Badge'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Driver Badge";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
				//Get particulars [Conductors Badge]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Conductors Badge'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Conductors Badge";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
}


// 3.1 - Above   -  Price of vehicle below 1 million
if ($engine_size == "3.1 - Above" && $cost_price =="Price of vehicle below 1 million"){
	
		//Get particulars [Registration Book]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Registration Book'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Registration Book";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Inspection Fee]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Inspection Fee'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Inspection Fee";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Proof of ownership]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Proof of ownership'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Proof of ownership";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [New Plate Number]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='New Plate Number'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "New Plate Number";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Price of vehicle below 1 million]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Price of vehicle below 1 million'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Registration for Price of vehicle below 1 million";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Certificate of road worthiness]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Certificate of road worthiness'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Certificate of road worthiness";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_6months','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Vehicle License [3.1 - above]]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Vehicle License [3.1 - above]'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Vehicle License [3.1 - above]";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
						//Get particulars [Hackney permit]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Hackney permit'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Hackney permit";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
		//Get particulars [Driver Badge]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Driver Badge'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Driver Badge";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
				//Get particulars [Conductors Badge]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Conductors Badge'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Conductors Badge";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
}

//Get particulars [SMS Alert]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='SMS Alert'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "SMS Alert";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
		//Get particulars [Stamp Duty]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Commercial Pickup/Bus' AND `particulars`='Stamp Duty'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Stamp Duty";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);

?>