from django.db import models
from django.contrib.auth.models import User
from commons.utility import upload_file_path, upload_image_path

from core.models import BaseModel, BaseModelWithAuthor, ProfileBaseModel
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class EmployeeJobManager(models.Manager):
    def filter_by_name(self, name):
        return self.filter(name__icontains=name)
    
# 1
class EmployeeJob(BaseModel):
    name = models.CharField(max_length=20, null=True)
    note = models.TextField()

    objects = EmployeeJobManager()

    def __str__(self):
        return self.name


class DepartmentManager(models.Manager):
    def filter_by_name(self, name):
        return self.filter(name__icontains=name)  
# 2
class Department(BaseModelWithAuthor):
    number = models.IntegerField()
    name = models.CharField(max_length=20, null=True)
    director_name = models.CharField(max_length=20, null=True)
    note = models.TextField(null=True , blank=True)

    objects = DepartmentManager()

    def __str__(self):
        return self.name


class EmployeeManager(models.Manager):
    def filter_by_name(self, name):
        return self.filter(name__icontains=name)  

# 3
class Employee(ProfileBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)
    mother_name = models.CharField(max_length=20, null=True)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE)
    date_joining = models.DateTimeField( auto_now_add=True,null=True, blank=True) # 
    picture = models.ImageField(upload_to=upload_image_path,null=True, blank=True)
    job = models.ForeignKey(EmployeeJob,null=True, blank=True, on_delete=models.CASCADE)
    salary = models.CharField(max_length=20, null=True, blank=True)
    archive = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    objects = EmployeeManager()

    def __str__(self):
        return self.name
    
# 4
class EmployeeDocument(BaseModel):
    name = models.CharField(max_length=20, null=True ,blank=True)
    file = models.FileField(upload_to=upload_file_path, null=True, blank=True)
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)


# 5
class EmployeeSalary(models.Model):
    year = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)
    total_salary = models.CharField(max_length=15, null=True ,blank=True)
    total_deduction = models.CharField(max_length=15, null=True, blank=True)

# 6
class DeductionType(models.Model):
    number = models.IntegerField(null=True , blank=True)
    name = models.CharField(max_length=20, null=True, blank=True)

# 7
class Currency(models.Model):
    name = models.CharField(max_length=20, null=True)
    price = models.DecimalField(decimal_places=3, max_digits=8) #  null=True , blank=True

# 8
class DeductionSalary(models.Model):
    year = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    type_deduction = models.ForeignKey(DeductionType, null=True, blank=True, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, null=True, blank=True, on_delete=models.CASCADE)
    amount = models.CharField(max_length=15, null=True, blank=True)

# 9
class VacationType(models.Model):
    name = models.CharField(max_length=20, null=True ,blank=True)
    limit_days = models.IntegerField(null=True , blank=True)

# 10
class VacationRecord(models.Model):
    date_from = models.DateField(null=True,blank=True)
    date_to = models.DateField(null=True,blank=True)
    vacation_type = models.ForeignKey(VacationType, null=True, blank=True, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)
    duration = models.IntegerField(null=True, blank=True)


# 11
class WorkingTime(models.Model):
    date = models.DateField(null=True,blank=True)
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)
    entry_time = models.TimeField(null=True, blank=True)
    checkout_time = models.TimeField(null=True, blank=True)
    note = models.TextField(null=True , blank=True)
    work_day = models.BooleanField(default=False)
    work_type = models.CharField(max_length=100, null=True ,blank=True)