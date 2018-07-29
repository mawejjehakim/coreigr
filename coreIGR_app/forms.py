from django.forms import ModelForm
from django import forms
# from django.contrib.auth.models import User
from coreIGR_app.models import User, Office, Company, Vehicle, Individual, NumberPlate, StateCode, LocalGovArea, Charge, AssignedTin, InstitutionCategory, InstitutionType, MDA


 
class LoginForm(ModelForm):
	class Meta:
		model = User
		# fields = ('user_name', 'password')
		fields = ('password',)


class CleanSingleFieldForm(forms.Form):
    tin_number = forms.CharField( max_length=40 )


class UserForm(ModelForm):
	class Meta:
		model = User		
		fields = ('full_name', 'department', 'user_name', 'access_level')

class OfficeForm(forms.Form):
    office_name = forms.CharField( max_length=150)

class LocalGovAreaForm(forms.Form):
    local_government_name = forms.CharField( max_length=50)
    local_government_code = forms.CharField( max_length=10)


class StateCodeForm(ModelForm):
	class Meta:
		model = StateCode		
		fields = ('state_code',)


class ChargeForm(ModelForm):
	class Meta:
		model = Charge
		fields =( 'options', 'vehicle_type', 'particulars', 'amount')

class IndividualForm(ModelForm):
	"""docstring for IndivualRegistration"""
	class Meta:
		model = Individual			 
		fields = ('name', 'gender', 'date_of_birth', 'marital_status', 'state', 'address', 'email', 'occupation', 'employment_status', 'work_place', 'phone' )

class CompanyForm(ModelForm):
	class Meta:
		model = Company
		fields = ('institution', 'bussiness_status', 'bussiness_class','registration_number', 'bussiness_ownership_type', 'bussiness_name', 'bussiness_owner', 'bussiness_address', 'phone_number', 'email' ) 


class TinNumberForm(ModelForm):
	class Meta:
		model = AssignedTin
		fields = ('tin', )


class VehicleForm(ModelForm):
	class Meta:
		model = Vehicle
		fields =('chassis_number', 'vehicle_model', 'number_plate', 'vehicle_category', 'gross_weight', 'net_weight', 'no_of_passengers', 'colour',  )


class InstitutionCategoryForm(ModelForm):
	class Meta:
		model = InstitutionCategory
		fields = ('category_name', )


class InstitutionTypeForm(ModelForm):
	class Meta:
		model = InstitutionType
		fields = ('type_name', )


class SingleValueCharFieldForm(ModelForm):
	class Meta:
		model = InstitutionType
		fields = ('type_name', )

class MDAForm(ModelForm):
	class Meta:
		model = MDA
		fields = ('mda_name', )

class PlateNumberForm(ModelForm):
	class Meta:
		model = NumberPlate
		fields = ('number_plate', )


