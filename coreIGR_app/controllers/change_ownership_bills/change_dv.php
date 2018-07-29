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

	
		//Get particulars [Registration Fee]
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Dealers Vehicle' AND `particulars`='Registration Fee'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Registration Fee";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		

//Get particulars [SMS Alert]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Dealers Vehicle' AND `particulars`='SMS Alert'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "SMS Alert";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);
		
		
		//Get particulars [Stamp Duty]
	$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='New' AND `vehicle_type`='Dealers Vehicle' AND `particulars`='Stamp Duty'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Stamp Duty";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) 		        VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Change of ownership','Not Paid','$staff','$office')";
		$qur = mysqli_query($conn,$ins);

?>