from django.contrib import admin
from .models import Doctor,Patient,Appointment,PatientDischargeDetails,Referral,InternalReferral


# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)

class ReferralAdmin(admin.ModelAdmin):
    pass
admin.site.register(Referral, ReferralAdmin)

class InternalReferralAdmin(admin.ModelAdmin):
    pass
admin.site.register(InternalReferral, InternalReferralAdmin)