from enum import auto
from django.db import models
from django.contrib.auth.models import User

departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

treatments=[('Ongoing','Ongoing'),
('Stopped','Stopped')
]

reason=[('Inpatient','Inpatient'),
('OutPatient','OutPatient'),
('Community','Communnity')
]

mobility=[('Bed Bound','Bed Bound'),
('Wheelchair','Wheelchair'),('Crutches','Crutches'),
('Walking Frame','Walking Frame'),
('Requires Assistance','Requires Assistance'),
('Independent','Independent')
]

selfcare=[('Carer Dependent','Carer Dependent'),
('Requires Commode','Requires Commode'),
('Requires Modified Washroom','Requires Modified Washroom'),
('Independent','Independent')
]

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)



class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.IntegerField(null=False)
    symptoms = models.CharField(max_length=100,null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+" ("+self.symptoms+")"


class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)

class InternalReferral(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    referralDate=models.DateField(auto_now=True)
    referralReason=models.TextField(max_length=500)
    primaryDiagnose=models.CharField(max_length=200,null=True)
    treatments=models.CharField(max_length=200,null=True)
    status=models.BooleanField(default=False)


class Referral(models.Model):
    date=models.DateField(null=True)
    referralTo=models.CharField(max_length=100,null=True)
    focalPoint=models.CharField(max_length=100,null=True)
    referralPhone=models.CharField(max_length=10,null=True)
    referralAddress=models.CharField(max_length=100,null=True)
    referralEmail=models.EmailField(null=True)
    
    referringFrom=models.CharField(max_length=100,null=True)
    foculPoint1=models.CharField(max_length=100,null=True)
    referringPhone=models.CharField(max_length=10,null=True)
    referringAddress=models.CharField(max_length=100,null=True)
    referringEmail=models.EmailField(null=True)
    
    patientId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    patientNumber=models.CharField(max_length=10,null=True)
    dob=models.DateField(null=True)
    gender=models.CharField(max_length=1,null=True)
    patientAddress=models.CharField(max_length=100,null=True)
    
    primaryDiagnose=models.CharField(max_length=100,null=True)
    otherDiagnose=models.CharField(max_length=100,null=True)
    treatments=models.CharField(max_length=100,null=True,choices=treatments,default='Ongoing')
    referralReason=models.CharField(max_length=100,null=True,choices=reason, default='Inpatient')
    transportationNeeds=models.CharField(max_length=100,null=True)
    followupRequirements=models.CharField(max_length=100,null=True)
    mobility=models.CharField(max_length=100,null=True,choices=mobility,default='Bed Bound')
    precautions=models.CharField(max_length=100,null=True)
    selfCare=models.CharField(max_length=100,null=True,choices=selfcare,default='Carer Dependent')
    coginitiveImpairment=models.CharField(max_length=100,null=True)
    
    #patientId=models.PositiveIntegerField(null=True)
    #doctorId=models.PositiveIntegerField(null=True)
    #referTo=models.CharField(max_length=100,null=True)
    #referFrom=models.CharField(max_length=100,null=True)
    #kin=models.CharField(max_length=40,null=True)
    #patientCondition=models.CharField(max_length=100,null=True)
    #history=models.TextField(max_length=500,null=True)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.date+" "+self.referralTo+" "+self.referringFrom+" "+self.patientName+" "+self.selfCare



class PatientDischargeDetails(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40)
    assignedDoctorName=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    symptoms = models.CharField(max_length=100,null=True)

    admitDate=models.DateField(null=False)
    releaseDate=models.DateField(null=False)
    daySpent=models.PositiveIntegerField(null=False)

    roomCharge=models.PositiveIntegerField(null=False)
    medicineCost=models.PositiveIntegerField(null=False)
    doctorFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)


    
