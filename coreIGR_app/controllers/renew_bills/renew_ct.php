<?php

// GENERATE BILL

//Get particulars [Vehicle License [6 - 8 tyres]]
		if($assessment == "Vehicle License [6 - 8 tyres]"){
			
			 //Check if Particulars have expired:
		$sqll = "SELECT `status` FROM `tbl_coreigr_assessment_transactions` WHERE `chassis`='$chassis' AND `particulars`='$assessment' AND `status`='Active'";
		$qurr = mysqli_fetch_array(mysqli_query($conn,$sqll));
		if($qurr['status'] == "Active"){
		$_SESSION['msg_title'] = "Error!";
		$_SESSION['msg'] = "This particulars has not expired!";
		$_SESSION['btn'] = "Try Again";
		$_SESSION['return_url'] = "vehicle_assessment.php#invoice";
		header ("Location: msgbox.php");
		exit;
		}
		
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='Renew' AND `vehicle_type`='Commercial Truck/Trailer/Lorry/Tipper' AND 
		`particulars`='Vehicle License [6 - 8 tyres]'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Vehicle License [6 - 8 tyres]";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Renewal of Particulars','Not Paid','$staff','$office')";
		mysqli_query($conn,$ins);		
				
				
		}

//Get particulars [Vehicle License [10 tyres - above]]
		if($assessment == "Vehicle License [10 tyres - above]"){
			
			 //Check if Particulars have expired:
		$sqll = "SELECT `status` FROM `tbl_coreigr_assessment_transactions` WHERE `chassis`='$chassis' AND `particulars`='$assessment' AND `status`='Active'";
		$qurr = mysqli_fetch_array(mysqli_query($conn,$sqll));
		if($qurr['status'] == "Active"){
		$_SESSION['msg_title'] = "Error!";
		$_SESSION['msg'] = "This particulars has not expired!";
		$_SESSION['btn'] = "Try Again";
		$_SESSION['return_url'] = "vehicle_assessment.php#invoice";
		header ("Location: msgbox.php");
		exit;
		}
		
				$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='Renew' AND `vehicle_type`='Commercial Truck/Trailer/Lorry/Tipper' AND 
		`particulars`='Vehicle License [10 tyres - above]'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Vehicle License [10 tyres - above]";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Renewal of Particulars','Not Paid','$staff','$office')";
		mysqli_query($conn,$ins);
		
		}


//Get particulars Certificate of road worthiness
              if($assessment == "Certificate of road worthiness"){
				  
				   //Check if Particulars have expired:
		$sqll = "SELECT `status` FROM `tbl_coreigr_assessment_transactions` WHERE `chassis`='$chassis' AND `particulars`='$assessment' AND `status`='Active'";
		$qurr = mysqli_fetch_array(mysqli_query($conn,$sqll));
		if($qurr['status'] == "Active"){
		$_SESSION['msg_title'] = "Error!";
		$_SESSION['msg'] = "This particulars has not expired!";
		$_SESSION['btn'] = "Try Again";
		$_SESSION['return_url'] = "vehicle_assessment.php#invoice";
		header ("Location: msgbox.php");
		exit;
		}
		
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='Renew' AND `vehicle_type`='Commercial Truck/Trailer/Lorry/Tipper' AND 
		`particulars`='Certificate of road worthiness'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Certificate of road worthiness";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_6months','Renewal of Particulars','Not Paid','$staff','$office')";
		mysqli_query($conn,$ins);				  
				  
			  }
			  
//Get particulars Proof of ownership			  
              if($assessment == "Proof of ownership"){
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='Renew' AND `vehicle_type`='Commercial Truck/Trailer/Lorry/Tipper' AND 
		`particulars`='Proof of ownership'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Proof of ownership";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Renewal of Particulars','Not Paid','$staff','$office')";
		mysqli_query($conn,$ins);					  
			  }
//Get particulars New Plate Number				  
			  if($assessment == "New Plate Number"){
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='Renew' AND `vehicle_type`='Commercial Truck/Trailer/Lorry/Tipper' AND 
		`particulars`='New Plate Number'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "New Plate Number";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Renewal of Particulars','Not Paid','$staff','$office')";
		mysqli_query($conn,$ins);					  
			  }
//Get particulars Registration Book				  
              if($assessment == "Registration Book"){
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='Renew' AND `vehicle_type`='Commercial Truck/Trailer/Lorry/Tipper' AND 
		`particulars`='Registration Book'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Registration Book";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Renewal of Particulars','Not Paid','$staff','$office')";
		mysqli_query($conn,$ins);	
			  }
	
//Get particulars Driver Badge

 if($assessment == "Driver Badge"){
	 
	  //Check if Particulars have expired:
		$sqll = "SELECT `status` FROM `tbl_coreigr_assessment_transactions` WHERE `chassis`='$chassis' AND `particulars`='$assessment' AND `status`='Active'";
		$qurr = mysqli_fetch_array(mysqli_query($conn,$sqll));
		if($qurr['status'] == "Active"){
		$_SESSION['msg_title'] = "Error!";
		$_SESSION['msg'] = "This particulars has not expired!";
		$_SESSION['btn'] = "Try Again";
		$_SESSION['return_url'] = "vehicle_assessment.php#invoice";
		header ("Location: msgbox.php");
		exit;
		}
		
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='Renew' AND `vehicle_type`='Commercial Truck/Trailer/Lorry/Tipper' AND 
		`particulars`='Driver Badge'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Driver Badge";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Renewal of Particulars','Not Paid','$staff','$office')";
		mysqli_query($conn,$ins);	
			  }
//Get particulars Hackney permit [6 - 8 tyres]
if($assessment == "Hackney permit [6 - 8 tyres]"){
	
	 //Check if Particulars have expired:
		$sqll = "SELECT `status` FROM `tbl_coreigr_assessment_transactions` WHERE `chassis`='$chassis' AND `particulars`='$assessment' AND `status`='Active'";
		$qurr = mysqli_fetch_array(mysqli_query($conn,$sqll));
		if($qurr['status'] == "Active"){
		$_SESSION['msg_title'] = "Error!";
		$_SESSION['msg'] = "This particulars has not expired!";
		$_SESSION['btn'] = "Try Again";
		$_SESSION['return_url'] = "vehicle_assessment.php#invoice";
		header ("Location: msgbox.php");
		exit;
		}
		
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='Renew' AND `vehicle_type`='Commercial Truck/Trailer/Lorry/Tipper' AND 
		`particulars`='Hackney permit [6 - 8 tyres]'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Hackney permit [6 - 8 tyres]";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Renewal of Particulars','Not Paid','$staff','$office')";
		mysqli_query($conn,$ins);	
			  }
			  
//Get particulars Hackney permit [10 tyres - above]
if($assessment == "Hackney permit [10 tyres - above]"){
	
	 //Check if Particulars have expired:
		$sqll = "SELECT `status` FROM `tbl_coreigr_assessment_transactions` WHERE `chassis`='$chassis' AND `particulars`='$assessment' AND `status`='Active'";
		$qurr = mysqli_fetch_array(mysqli_query($conn,$sqll));
		if($qurr['status'] == "Active"){
		$_SESSION['msg_title'] = "Error!";
		$_SESSION['msg'] = "This particulars has not expired!";
		$_SESSION['btn'] = "Try Again";
		$_SESSION['return_url'] = "vehicle_assessment.php#invoice";
		header ("Location: msgbox.php");
		exit;
		}
		
		
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='Renew' AND `vehicle_type`='Commercial Truck/Trailer/Lorry/Tipper' AND 
		`particulars`='Hackney permit [10 tyres - above]'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Hackney permit [10 tyres - above]";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Renewal of Particulars','Not Paid','$staff','$office')";
		mysqli_query($conn,$ins);	
			  }


//Get particulars Conductors Badge
if($assessment == "Conductors Badge"){
	
	 //Check if Particulars have expired:
		$sqll = "SELECT `status` FROM `tbl_coreigr_assessment_transactions` WHERE `chassis`='$chassis' AND `particulars`='$assessment' AND `status`='Active'";
		$qurr = mysqli_fetch_array(mysqli_query($conn,$sqll));
		if($qurr['status'] == "Active"){
		$_SESSION['msg_title'] = "Error!";
		$_SESSION['msg'] = "This particulars has not expired!";
		$_SESSION['btn'] = "Try Again";
		$_SESSION['return_url'] = "vehicle_assessment.php#invoice";
		header ("Location: msgbox.php");
		exit;
		}
		
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='Renew' AND `vehicle_type`='Commercial Truck/Trailer/Lorry/Tipper' AND 
		`particulars`='Conductors Badge'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Conductors Badge";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Renewal of Particulars','Not Paid','$staff','$office')";
		mysqli_query($conn,$ins);	
			  }
			  
//Get particulars SMS Alert
if($assessment == "SMS Alert"){
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='Renew' AND `vehicle_type`='Commercial Truck/Trailer/Lorry/Tipper' AND 
		`particulars`='SMS Alert'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "SMS Alert";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Renewal of Particulars','Not Paid','$staff','$office')";
		mysqli_query($conn,$ins);	
			  }
			  

//Get particulars Stamp Duty
if($assessment == "Stamp Duty"){
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='Renew' AND `vehicle_type`='Commercial Truck/Trailer/Lorry/Tipper' AND 
		`particulars`='Stamp Duty'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Stamp Duty";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Renewal of Particulars','Not Paid','$staff','$office')";
		mysqli_query($conn,$ins);	
			  }	
?>