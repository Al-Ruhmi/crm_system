
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.


User = get_user_model()

class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    modified_on = models.DateTimeField(auto_now=True)
    class Meta:
       abstract = True


class BaseModelWithAuthor(BaseModel):
   created_by = models.ForeignKey(settings.AUTH_USER_MODEL,  related_name='%(class)s_createdby', null=True,blank=True, on_delete=models.CASCADE)
   modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_modifiedby', null=True,blank=True, on_delete=models.CASCADE)
   class Meta:
       abstract = True


class AddressBaseModel(models.Model):
    address1          = models.CharField(max_length=255, blank=True, null=True)
    address2          = models.CharField(max_length=255, blank=True, null=True)
    # country           = models.CharField(max_length=32, choices=COUNTRY_CHOICES, blank=True)
    state             = models.CharField(max_length=255, blank=True, null=True)
    city              = models.CharField(max_length=255, blank=True, null=True)
    zip_code          = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True


class ProfileBaseModel(models.Model):
    user              = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE, primary_key=True)
    first_name        = models.CharField(max_length=255, blank=True, null=True)
    last_name        = models.CharField(max_length=255, blank=True, null=True)
    gender            = models.CharField(max_length=32, choices=(('Male','Male'),('Female','Female')), blank=True)
    date_of_birth     = models.DateField( blank=True, null=True)
    email             = models.CharField(max_length=255, blank=True, null=True)
    phone_number        = models.CharField(max_length=255, blank=True, null=True)
    # country           = models.CharField(max_length=32, choices=COUNTRY_CHOICES, blank=True)
    state             = models.CharField(max_length=255, blank=True, null=True)
    city              = models.CharField(max_length=255, blank=True, null=True)
    zip_code          = models.CharField(max_length=255, blank=True, null=True)
    about             = models.TextField(blank=True, null=True)
    contact_details   = models.TextField(blank=True, null=True)
    latitude          = models.CharField(max_length=512, blank=True, null=True)
    longitude         = models.CharField(max_length=512, blank=True, null=True)
    class Meta:
       abstract = True



# أنواع الشركات - شركه مساهمه - شركة أفراد - ..
class BusinessType(models.Model):
    name =  models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    def str(self):
        return self.name

# كلاس للشركه التي تملك المشروع
class Company(models.Model):
    name                   =  models.CharField(max_length=255, blank=True, null=True)
    description            = models.TextField(blank=True, null=True)
    email                  = models.CharField(max_length=255, blank=True, null=True)
    cell_phone             = models.CharField(max_length=255, blank=True, null=True)
    land_phone             = models.CharField(max_length=255, blank=True, null=True)
    # country                = models.CharField(max_length=32, choices=COUNTRY_CHOICES, blank=True)
    state                  = models.CharField(max_length=255, blank=True, null=True)
    city                   = models.CharField(max_length=255, blank=True, null=True)
    zip_code               = models.CharField(max_length=255, blank=True, null=True)
    about                  = models.TextField(blank=True, null=True)
    contact_details        = models.TextField(blank=True, null=True)
    latitude               = models.CharField(max_length=512, blank=True, null=True)
    longitude              = models.CharField(max_length=512, blank=True, null=True)
    year_established       =  models.DateField( blank=True, null=True)
    total_employees        =  models.CharField(max_length=255, blank=True, null=True)
    business_type     = models.ForeignKey(BusinessType, related_name="CompanyBusinessType", blank=True, null=True,on_delete=models.CASCADE)
    main_products          =  models.CharField(max_length=255, blank=True, null=True)
    url                    =  models.CharField(max_length=255, blank=True, null=True)
    social_link            =  models.CharField(max_length=255, blank=True, null=True)

    def str(self):
        return self.name