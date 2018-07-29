<?php 
session_start(); 
include_once("checksession.php");
include_once("../dbconnect.php");
$tin = $_SESSION['Opt_Value'];


$sql = "SELECT * FROM `tbl_coreigr_reg_ind` WHERE `tin`='$tin'";
$row = (mysqli_fetch_array(mysqli_query($conn,$sql)));

$tin = $row['tin'];
$name = $row['name'];
$title = $row['title'];

if($tin ==""){
	$_SESSION['msg_title'] = "RECORD NOT FOUND!";
	$_SESSION['msg'] = "Invalid TIN Number!";
	$_SESSION['btn'] = "Try Again";
	$_SESSION['return_url'] = "get_tin_vehicle_change.php";
	header ("Location: msgbox.php");
	exit;
}

$_SESSION['reg_tin'] = $tin;
$_SESSION['reg_title'] = $title;
$_SESSION['reg_name'] = $name;

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>CoreIGR | </title>

    <!-- Bootstrap Core CSS -->
    <link href="../../css/bootstrap.min.css" rel="stylesheet">

    <!-- MetisMenu CSS -->
    <link href="../../css/metisMenu.min.css" rel="stylesheet">

    <!-- Timeline CSS -->
    <link href="../../css/timeline.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="../../css/startmin.css" rel="stylesheet">

    <!-- Morris Charts CSS -->
    <link href="../../css/morris.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="../../css/font-awesome.min.css" rel="stylesheet" type="text/css">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
</head>
<body>

<div id="wrapper">

    <!-- Navigation -->
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="navbar-header">
            <a class="navbar-brand" href="#">Core-IGR</a>
        </div>

        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
        </button>

        <!-- Top Navigation: Left Menu -->
        <ul class="nav navbar-nav navbar-left navbar-top-links">
            <li><a href="../../index.html"><i class="fa fa-home fa-fw"></i> Website</a></li>
        </ul>

        <!-- Top Navigation: Right Menu -->
        <ul class="nav navbar-right navbar-top-links">
            <li class="dropdown navbar-inverse">
                <a class="dropdown-toggle" data-toggle="dropdown" href="#">
                    <i class="fa fa-bell fa-fw"></i> <b class="caret"></b>
                </a>
                <ul class="dropdown-menu dropdown-alerts">
                    <li>
                        <a href="#">
                            <div>
                                <i class="fa fa-comment fa-fw"></i> New Comment
                                <span class="pull-right text-muted small">4 minutes ago</span>
                            </div>
                        </a>
                    </li>
                    <li class="divider"></li>
                    <li>
                        <a class="text-center" href="#">
                            <strong>See All Alerts</strong>
                            <i class="fa fa-angle-right"></i>
                        </a>
                    </li>
                </ul>
            </li>
            <li class="dropdown">
                <a class="dropdown-toggle" data-toggle="dropdown" href="#">
                    <i class="fa fa-user fa-fw"></i> <?php echo $_SESSION['myfullname']; ?> <b class="caret"></b>
                </a>
                <ul class="dropdown-menu dropdown-user">
                    <li><a href="#"><i class="fa fa-user fa-fw"></i> Change Password</a>
                    </li>
                    <li class="divider"></li>
                    <li><a href="../logout.php"><i class="fa fa-sign-out fa-fw"></i> Logout</a>
                    </li>
                </ul>
            </li>
        </ul>

        <!-- Sidebar -->
        <div class="navbar-default sidebar" role="navigation">
            <div class="sidebar-nav navbar-collapse">

                <ul class="nav" id="side-menu">
                    <li class="sidebar-search">
                        <div class="input-group custom-search-form">
                            <input type="text" class="form-control" placeholder="Search...">
                                <span class="input-group-btn">
                                    <button class="btn btn-primary" type="button">
                                        <i class="fa fa-search"></i>
                                    </button>
                                </span>
                        </div>
                    </li>
                     <li>
                                <a href="../main.php"><i class="fa fa-home fa-fw"></i> Home</a>
                            </li>
                            <li>
                                <a href="../logout.php"><i class="fa fa-power-off fa-fw"></i> Logout</a>
                            </li>
                                </ul>
                            </li>
                </ul>

            </div>
        </div>
    </nav>

    <!-- Page Content -->
    <div id="page-wrapper">
        <div class="container-fluid">

            <div class="row">
                <div class="col-lg-12">
                    <h1 class="page-header">CHANGE OF OWNERSHIP</h1>
                </div>
            </div>

            <!-- ... Your content goes here ... -->
<div class="col-lg-8">
                        <div class="panel panel-green">
                            <div class="panel-heading">
                                Personal Information
                          </div>
                            <div class="panel-body">
                                <table width="400" border="1" class="table table-striped table-bordered table-hover">
                                  <tr>
                                    <td width="20%">TIN:</td>
                                    <td width="55%"><strong><?php echo $row['tin']; ?>&nbsp;</strong></td>
                                    <td width="25%" rowspan="6"><img name="" src="../tin/images/passports/<?php echo $row['passport'] ?>" width="300" height="200" alt=""></td>
                                  </tr>
                                  <tr>
                                    <td>Name:</td>
                                    <td><strong><?php echo $row['title']; ?> <?php echo $row['name']; ?></strong></td>
                                  </tr>
                                  <tr>
                                    <td>Gender:</td>
                                    <td><strong><?php echo $row['gender']; ?></strong></td>
                                  </tr>
                                  <tr>
                                    <td>State of Origin:</td>
                                    <td><strong><?php echo $row['state']; ?></strong></td>
                                  </tr>
                                  <tr>
                                    <td>Residential Address:</td>
                                    <td><strong><?php echo $row['address']; ?></strong></td>
                                  </tr>
                                  <tr>
                                    <td>Phone No:</td>
                                    <td><strong><?php echo $row['phone']; ?></strong></td>
                                  </tr>
                                </table>
                                <p>&nbsp;</p>
                            </div>
                            
        </div>
                        <!-- /.col-lg-4 -->
                    </div>
                    <div class="col-lg-8">
                        <div class="panel panel-green">
                            <div class="panel-heading">
                                Select Vehicle
                          </div>
                            <div class="panel-body">
                                <p><span class="col1">
                                  <?php 
$sql = "SELECT * FROM `tbl_coreigr_vehicle_info` WHERE `tin_current_owner`='$tin'";
$exec = mysqli_query($conn,$sql);

echo "</table><br>";
echo "<table width='600' border='1' class='table table-striped table-bordered table-hover'>";  
echo "<tr>"; 
echo "<td><div align='Left'><strong>Opt:</strong></div></td>";
echo "<td><div align='Left'><strong>Chassis No:</strong></div></td>";
echo "<td><div align='Left'><strong>Vehicle type:</strong></div></td>";
echo "<td><div align='Left'><strong>Number Plate:</strong></div></td>";
echo "<td><div align='Left'><strong>Category:</strong></div></td>";
echo "<td><div align='Left'><strong>Color:</strong></div></td>";
echo "</tr>";
$i = 0;
$c = 1;
while($row = mysqli_fetch_array($exec)){
echo "<td><div align='Left'><strong><a href='change_vehicle_details.php?chassis=".$row["chassis"]."'>Select</a></strong></div></td>";
echo "<td><div align='Left'>".$row["chassis"]."</div></td>";
echo "<td><div align='Left'>".$row["vehicle_type"]."</div></td>";
echo "<td><div align='Left'>".$row["number_plate"]."</div></td>";
echo "<td><div align='Left'>".$row["category"]."</div></td>";
echo "<td><div align='Left'>".$row["color"]."</div></td>";
echo "</tr>";
$i++;
$c++;
}

?>
                                </span></p>
                            </div>
                            
                      </div>
                        <!-- /.col-lg-4 -->
                    </div>
        </div>
    </div>

</div>

<!-- jQuery -->
<script src="../../js/jquery.min.js"></script>

<!-- Bootstrap Core JavaScript -->
<script src="../../js/bootstrap.min.js"></script>

<!-- Metis Menu Plugin JavaScript -->
<script src="../../js/metisMenu.min.js"></script>

<!-- Custom Theme JavaScript -->
<script src="../../js/startmin.js"></script>

</body>
</html>
