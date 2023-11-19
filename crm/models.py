from django.db import models
from django.contrib.auth.models import User
from hr.models import Employee

from core.models import AddressBaseModel, BaseModel, BaseModelWithAuthor, BusinessType, Company, ProfileBaseModel
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

User = get_user_model()

# 1
class Customer(ProfileBaseModel):
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    business_type = models.ForeignKey(BusinessType, null=True, blank=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

# 2
class CustomerAddress(AddressBaseModel):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    basic = models.BooleanField()

# 3
class CustomerCustomField(BaseModel):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    value = models.CharField(max_length=255, null=True)

# 4
class CustomerContract(BaseModelWithAuthor):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    number = models.IntegerField(null=True , blank=True)
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    data = models.TextField(null=True,blank=True)
    active = models.BooleanField(default=True)

# 5
class CrmTeam(BaseModel):
    name = models.CharField(max_length=255, null=True)
    group_team = models.CharField(max_length=255, null=True)
    lead = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)

# 6
class CrmMember(BaseModel):
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)
    team = models.ForeignKey(CrmTeam, null=True, blank=True, on_delete=models.CASCADE)

# 7
class TaskStatus(BaseModel):
    name = models.CharField(max_length=255, null=True)
    color = models.CharField(max_length=255, null=True)
    postition = models.IntegerField(null=True , blank=True)

    priority = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

# 8
class TaskClassification(BaseModel):
    name = models.CharField(max_length=255, null=True)
    color = models.CharField(max_length=255, null=True)
    postition = models.IntegerField(null=True , blank=True)


# 9
class TaskCustomField(BaseModel):
    task = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    value = models.CharField(max_length=255, null=True)




# 10
class CrmProject(BaseModelWithAuthor):
    name = models.CharField(max_length=255, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(CrmMember, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(null=True,blank=True)
    due_date = models.DateField(null=True, blank=True) # 
    icon = models.ImageField(upload_to='crm/static/crm_img/images/',null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    for_employee = models.BooleanField()
    for_customer = models.BooleanField()
    active = models.BooleanField(default=True)

# 11
class Task(BaseModelWithAuthor):
    number = models.IntegerField(null=True , blank=True)

    status = models.ForeignKey(TaskStatus, null=True, blank=True, on_delete=models.CASCADE)
    classification = models.ForeignKey(TaskClassification, null=True, blank=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    completed = models.BooleanField(default=False)

    project = models.ForeignKey(CrmProject, null=True, blank=True, on_delete=models.CASCADE)
    due_date = models.DateTimeField(null=True, blank=True)
    tags = models.TextField(null=True,blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    autidors = models.CharField(max_length=512, null=True)
    start_date_plan = models.DateTimeField(null=True,blank=True)
    end_date_plan = models.DateTimeField(null=True,blank=True)
    data = models.TextField(null=True,blank=True)
    allow_time_tracking = models.BooleanField(default=False)
    changed_by = models.ForeignKey( CrmMember, null=True, blank=True, on_delete=models.CASCADE)
    changed_date = models.DateTimeField(null=True,blank=True)


# 12
class TaskDocument(BaseModel):
    name = models.CharField(max_length=255, null=True)
    file = models.CharField(max_length=255, null=True)
    task = models.ForeignKey(Task, null=True, blank=True, on_delete=models.CASCADE)

# 13
class TaskActivity(BaseModel):
    task = models.ForeignKey(Task, null=True, blank=True, on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    member = models.ForeignKey(CrmMember, null=True, blank=True, on_delete=models.CASCADE)
    type_action = models.CharField(max_length=255, null=True)
    data_action = models.TextField(null=True,blank=True)

# 14
class TaskActivityDocument(BaseModel):
    name = models.CharField(max_length=255, null=True)
    file = models.CharField(max_length=255, null=True)
    activity = models.ForeignKey(TaskActivity, null=True, blank=True, on_delete=models.CASCADE)


# 15
class TaskResponsible(BaseModel):
    task = models.ForeignKey(Task, null=True, blank=True, on_delete=models.CASCADE)
    member = models.ForeignKey(CrmMember, null=True, blank=True, on_delete=models.CASCADE)
    can_read = models.BooleanField()
    can_write = models.BooleanField()

# 16
class TaskComment(BaseModel):
    task = models.ForeignKey(Task, null=True, blank=True, on_delete=models.CASCADE)
    member = models.ForeignKey(CrmMember, null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField(null=True,blank=True)
    file = models.CharField(max_length=255, null=True)
    edited = models.BooleanField(default=False)

# 17
class TaskWorkLog(BaseModel):
    task = models.ForeignKey(Task, null=True, blank=True, on_delete=models.CASCADE)
    member = models.ForeignKey(CrmMember, null=True, blank=True, on_delete=models.CASCADE)
    time = models.CharField(max_length=255, null=True)
    comment = models.TextField(null=True,blank=True)


# 18
class TaskColumn(BaseModel):
    name = models.CharField(max_length=255, null=True)
    tasks = models.CharField(max_length=512, null=True)
    color = models.CharField(max_length=255, null=True)
    position = models.CharField(max_length=255, null=True)

# 19
class TaskHistory(BaseModel):
    task = models.CharField(max_length=512, null=True)
    author = models.ForeignKey(CrmMember, null=True, blank=True, on_delete=models.CASCADE)
    field = models.CharField(max_length=255, null=True)
    data = models.TextField(null=True,blank=True)