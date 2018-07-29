<?php
	
	//Generate Expiration Dates 1 year
	$tdate = date("Y/m/d");
	$issuedate = date("Y/m/d");
	$y = date("Y") + 1;
	$m = date("m");
	$d = date("d");
	$expirationdate_1year = $y."/".$m."/".$d;
	
		
// GENERATE BILL

// 1.6 - 2.0   -  Above 1 million
if ($engine_size == "1.6 - 2.0" && $cost_price =="Price of vehicle above 1 million"){
	
		//Get particulars [Registration Book]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Registration Book'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Registration Book";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
		
		//Get particulars [Proof of ownership]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Proof of ownership'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Proof of ownership";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
		
		//Get particulars [Certificate of road worthiness]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Certificate of road worthiness'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Certificate of road worthiness";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Vehicle License [1.6 - 2.0]]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Vehicle License [1.6 - 2.0]'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Vehicle License [1.6 - 2.0]";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
}


// 2.1 - 3.0   -  Above 1 million
if ($engine_size == "2.1 - 3.0" && $cost_price =="Price of vehicle above 1 million"){
	
		//Get particulars [Registration Book]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Registration Book'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Registration Book";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
		
		//Get particulars [Proof of ownership]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Proof of ownership'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Proof of ownership";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
		
		
		
		//Get particulars [Certificate of road worthiness]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Certificate of road worthiness'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Certificate of road worthiness";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Vehicle License [2.1 - 3.0]]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Vehicle License [2.1 - 3.0]'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Vehicle License [2.1 - 3.0]";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
}


// 3.1 - Above   -  Above 1 million
if ($engine_size == "3.1 - Above" && $cost_price =="Price of vehicle above 1 million"){
	
		//Get particulars [Registration Book]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Registration Book'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Registration Book";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
		
		//Get particulars [Proof of ownership]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Proof of ownership'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Proof of ownership";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
		
		
		
		//Get particulars [Certificate of road worthiness]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Certificate of road worthiness'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Certificate of road worthiness";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Vehicle License [3.1 - Above]]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Vehicle License [3.1 - Above]'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Vehicle License [3.1 - Above]";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
}



//========================================================================================================================
// 1.6 - 2.0   -  Price of vehicle below 1 million
if ($engine_size == "1.6 - 2.0" && $cost_price =="Price of vehicle below 1 million"){
	
		//Get particulars [Registration Book]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Registration Book'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Registration Book";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
		
		//Get particulars [Proof of ownership]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Proof of ownership'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Proof of ownership";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
		
		
		
		//Get particulars [Certificate of road worthiness]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Certificate of road worthiness'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Certificate of road worthiness";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Vehicle License [1.6 - 2.0]]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Vehicle License [1.6 - 2.0]'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Vehicle License [1.6 - 2.0]";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
}


// 2.1 - 3.0   -  Price of vehicle below 1 million
if ($engine_size == "2.1 - 3.0" && $cost_price =="Price of vehicle below 1 million"){
	
		//Get particulars [Registration Book]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Registration Book'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Registration Book";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
		
		//Get particulars [Proof of ownership]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Proof of ownership'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Proof of ownership";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
		
		
		
		//Get particulars [Certificate of road worthiness]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Certificate of road worthiness'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Certificate of road worthiness";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Vehicle License [2.1 - 3.0]]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Vehicle License [2.1 - 3.0]'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Vehicle License [2.1 - 3.0]";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
}


// 3.1 - Above   -  Price of vehicle below 1 million
if ($engine_size == "3.1 - Above" && $cost_price =="Price of vehicle below 1 million"){
	
		//Get particulars [Registration Book]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Registration Book'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Registration Book";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
		
		//Get particulars [Proof of ownership]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Proof of ownership'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Proof of ownership";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
		
		
		
		//Get particulars [Certificate of road worthiness]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Certificate of road worthiness'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Certificate of road worthiness";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		//Get particulars [Vehicle License [3.1 - Above]]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Vehicle License [3.1 - Above]'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Vehicle License [3.1 - Above]";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
}



//Get particulars [SMS Alert]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='SMS Alert'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "SMS Alert";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
		//Get particulars [Stamp Duty]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Private Vehicle Saloon' AND `particulars`='Stamp Duty'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Stamp Duty";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Revalidation','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
?>