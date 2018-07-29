
from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
   
   	path('', views.login, name = "login"),
   	path('login/', views.login, name = "login"),

   	path('set-up/users/', views.all_users, name = "all_users" ),
   	path('set-up/add-user/', views.add_user, name = "add_user" ),
      path('set-up/institution-types/', views.all_institution_types, name = "all_institution_types" ),	
      path('set-up/institution-categories/', views.all_institution_categories, name = "all_institution_categories" ),  
      path('set-up/add-institution-category/', views.add_institution_category, name = "add_institution_category" ),  
      path('set-up/add-institution-type/', views.add_institution_type, name = "add_institution_type" ),  

      
 
   	path('set-up/lgas/', views.all_lgas, name = "all_lgas" ),
   	path('set-up/add-lga/', views.add_lga, name = "add_lga" ),
   	path('set-up/save-state-code/', views.save_state_code, name = "save_state_code" ),

   	path('set-up/charges/', views.all_charges, name = "all_charges"),
   	path('set-up/add-charge/', views.add_charge, name = "add_charge"),

   	path('set-up/offices/', views.all_offices, name = "all_offices" ),
   	path('set-up/add-office/', views.add_office, name = "add_office" ), 

      path('set-up/edit-office/<office_id>/', views.edit_office, name = "edit_office" ),
      path('set-up/update-office/', views.update_office, name = "update_office" ), 
      path('set-up/office/en-dis/<office_id>/', views.enable_dis_office, name = "enable_dis_office" ),


   	path('tin/companies/', views.all_companies, name = "all_companies" ),
      path('tin/add-company/', views.add_company, name = "add_company" ),
      path('tin/save-company/', views.save_company, name = "save_company" ),
      path('tin/company-preview/', views.c_data_preview_before_saving, name = "c_data_preview_before_saving" ),

   	path('tin/individuals/', views.all_individuals, name = "all_individuals" ),
      path('tin/add-individual/', views.add_individual, name = "add_individual" ),
      path('tin/save-individual/', views.save_individual, name = "save_individual" ),
   	path('tin/individual-preview/', views.i_data_preview_before_saving, name = "i_data_preview_before_saving" ),

      path('tin/edit-individual/<individual_id>/', views.edit_individual, name = "edit_individual" ),
      path('tin/update-individual/', views.update_individual, name = "update_individual" ),

      path('tin/edit-company/<company_id>/', views.edit_company, name = "edit_company" ),
      path('tin/update-company/', views.update_company, name = "update_company" ),
      # edit_individual_record.html


      path('mla/get-tin-info/', views.get_tin_info, name = "get_tin_info" ),
      path('mla/vehicles/', views.all_vehicles, name = "all_vehicles" ),
      path('mla/vehicle-preview/', views.v_data_preview_before_saving, name = "v_data_preview_before_saving" ),

      path('mla/change-vehicle-ownership/', views.change_vehicle_ownership, name = "change_vehicle_ownership" ),
      path('mla/mark-stolen-vehicle/', views.mark_stolen_vehicle, name = "mark_stolen_vehicle" ),
      path('mla/mark_vehicle/<plate_number>/', views.mark_vehicle, name="mark_vehicle"),
      # path('mla/get-learners-permit/', views.get_tin_info_learners_permit, name = "get_tin_info_learners_permit" ),
      path('mla/save-learners-permit/', views.save_learners_permit, name="save_learners_permit"),
      path('mla/get-vehicle-revalidation/', views.get_chassisnumber_info_vehicle_revalidation, name="get_chassisnumber_info_vehicle_revalidation"),
      path('mla/save-vehicle-revalidation/', views.save_vehicle_revalidation, name="save_vehicle_revalidation"),
      path('mla/get-vehicle-assessment/', views.get_chassisnumber_info_vehicle_assessment, name="get_chassisnumber_info_vehicle_assessment"),
      path('mla/save-vehicle-assessment/', views.save_vehicle_assessment, name="save_vehicle_assessment"),
      

      # path('mla/save-individual-vehicle/', views.save_vehicle, name = "save_vehicle" ),
    

   	# path('store/', views.store, )
      path('store/plate-numbers/', views.all_number_plates, name = "all_number_plates" ),
      path('store/add-number-plate/', views.add_number_plate, name = "add_number_plate" ),
      path('store/number-plate-preview/', views.p_n_data_preview_before_saving, name = "p_n_data_preview_before_saving" ),
      path('store/save-number-plate/', views.save_number_plate, name = "save_number_plate" ),
      path('store/get-office-name/', views.get_office_name, name = "get_office_name" ),
      path('store/get-lgov-numberplates/',views.get_lgov_numberplates, name = "get_lgov_numberplates"),
      path('store/issue-car-plate/<plate_number>/', views.issue_number_plate, name="issue_number_plate"),


      path('mda/mdas/', views.all_mdas, name = "all_mdas" ),
      path('mda/add-mda/',views.add_mda, name = "add_mda"),
      path('mda/revenue-items/',views.revenue_items, name = "revenue_items"),
      path('mda/genearate-bill/',views.genearate_bill, name = "genearate_bill"),
      path('mda/select-payment/',views.select_payement, name = "select_payement"),

      path('search/',views.search_record, name = "search_record")

      


   	# path('ml/', views.store, )


   	# path('super-admin/', views.store, )
   	
   	
   	]
