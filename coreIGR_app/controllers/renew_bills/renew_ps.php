<?php

// GENERATE BILL

//Get particulars [Vehicle License [1.6 - 2.0]]
		if($assessment == "Vehicle License [1.6 - 2.0]"){
			
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
			
			
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='Renew' AND `vehicle_type`='Private Vehicle Saloon' AND 
		`particulars`='Vehicle License [1.6 - 2.0]'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Vehicle License [1.6 - 2.0]";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Renewal of Particulars','Not Paid','$staff','$office')";
		mysqli_query($conn,$ins);		
				
				
		}

//Get particulars [Vehicle License [2.1 - 3.0]]
		if($assessment == "Vehicle License [2.1 - 3.0]"){
			
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
		
				$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='Renew' AND `vehicle_type`='Private Vehicle Saloon' AND 
		`particulars`='Vehicle License [2.1 - 3.0]'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Vehicle License [2.1 - 3.0]";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Renewal of Particulars','Not Paid','$staff','$office')";
		mysqli_query($conn,$ins);
		
		}

//Get particulars [Vehicle License [3.1 - Above]]				  
		if($assessment == "Vehicle License [3.1 - Above]"){
			
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
		
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='Renew' AND `vehicle_type`='Private Vehicle Saloon' AND 
		`particulars`='Vehicle License [3.1 - Above]'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Vehicle License [3.1 - Above]";
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
		
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='Renew' AND `vehicle_type`='Private Vehicle Saloon' AND 
		`particulars`='Certificate of road worthiness'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Certificate of road worthiness";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Renewal of Particulars','Not Paid','$staff','$office')";
		mysqli_query($conn,$ins);				  
				  
			  }
			  
//Get particulars Proof of ownership			  
              if($assessment == "Proof of ownership"){
				  
				  
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='Renew' AND `vehicle_type`='Private Vehicle Saloon' AND 
		`particulars`='Proof of ownership'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Proof of ownership";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','$expirationdate_1year','Renewal of Particulars','Not Paid','$staff','$office')";
		mysqli_query($conn,$ins);					  
			  }
//Get particulars New Plate Number				  
			  if($assessment == "New Plate Number"){
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='Renew' AND `vehicle_type`='Private Vehicle Saloon' AND 
		`particulars`='New Plate Number'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "New Plate Number";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Renewal of Particulars','Not Paid','$staff','$office')";
		mysqli_query($conn,$ins);					  
			  }
//Get particulars Registration Book				  
              if($assessment == "Registration Book"){
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='Renew' AND `vehicle_type`='Private Vehicle Saloon' AND 
		`particulars`='Registration Book'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Registration Book";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Renewal of Particulars','Not Paid','$staff','$office')";
		mysqli_query($conn,$ins);	
			  }
			  
//Get particulars SMS Alert
if($assessment == "SMS Alert"){
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='Renew' AND `vehicle_type`='Private Vehicle Saloon' AND 
		`particulars`='SMS Alert'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "SMS Alert";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Renewal of Particulars','Not Paid','$staff','$office')";
		mysqli_query($conn,$ins);	
			  }
			  

//Get particulars Stamp Duty
if($assessment == "Stamp Duty"){
		$sql = "SELECT * FROM `tbl_coreigr_charges` WHERE `opt`='Renew' AND `vehicle_type`='Private Vehicle Saloon' AND 
		`particulars`='Stamp Duty'";
		$row = mysqli_fetch_array(mysqli_query($conn,$sql));	
		$particulars = "Stamp Duty";
		$amount = $row['amount'];
		
		
		$ins = "INSERT INTO `tbl_coreigr_assessment_transactions`(`status`, `tcode`, `tin`, `chassis`, `particulars`, `amount`, `tdate`, `issue_date`, `expiration_date`, `transaction_type`, `payment_status`, `transaction_staff`, `transaction_office`) VALUES ('Active','$tcode','$tin','$chassis','$particulars','$amount','$tdate','$issuedate','-','Renewal of Particulars','Not Paid','$staff','$office')";
		mysqli_query($conn,$ins);	
			  }	
?>