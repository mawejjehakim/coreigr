from django.contrib import admin
from coreIGR_app.models import NumberPlate, LocalGovArea, Office, InstitutionCategory, InstitutionType, StateCode, AssignedTin, AssignedNumberPlate,  TransactionAssessment, Charge, User, ChargesOthers, LearnersPermit, Vehicle, Revalidation, Individual, Company, PayeeTaxpayer, MDAList, MDA, RevenueItem, MDAEbill

# Register your models here.
admin.site.register(TransactionAssessment)
admin.site.register(Charge)
admin.site.register(User)
admin.site.register(Office)
admin.site.register(AssignedTin)
admin.site.register(LocalGovArea)
admin.site.register(Vehicle)
admin.site.register(Individual)
 
admin.site.register(NumberPlate)
admin.site.register(RevenueItem) 
admin.site.register(StateCode) 
admin.site.register(InstitutionType) 
admin.site.register(InstitutionCategory) 
admin.site.register(AssignedNumberPlate)
 

admin.site.register(ChargesOthers)
admin.site.register(LearnersPermit)
admin.site.register(Revalidation)
admin.site.register(Company)
admin.site.register(PayeeTaxpayer)
admin.site.register(MDAList)
admin.site.register(MDA)
admin.site.register(MDAEbill)


 