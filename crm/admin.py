from django.contrib import admin

# Register your models here.
from .models import  CostCenter, Customer,CustomerAddress,CustomerCustomField,CustomerContract,CrmTeam,CrmMember,TaskStatus,TaskClassification,TaskCustomField,CrmProject,Task,TaskDocument,TaskActivity,TaskActivityDocument,TaskResponsible,TaskComment,TaskWorkLog,TaskColumn,TaskHistory,ClientActivityType,ClientActivity,ClientActivityAttribute,ClientActivityDocument
# Register your models here.



admin.site.register(Customer)
admin.site.register(CustomerAddress)
admin.site.register(CustomerCustomField)
admin.site.register(CustomerContract)
admin.site.register(CrmTeam)
admin.site.register(CrmMember)
admin.site.register(TaskStatus)
admin.site.register(TaskClassification)
admin.site.register(TaskCustomField)

admin.site.register(CrmProject)
admin.site.register(Task)
admin.site.register(TaskDocument)
admin.site.register(TaskActivity)
admin.site.register(TaskActivityDocument)
admin.site.register(TaskResponsible)
admin.site.register(TaskComment)
admin.site.register(TaskWorkLog)
admin.site.register(TaskColumn)
admin.site.register(TaskHistory)

admin.site.register(ClientActivityType)
admin.site.register(ClientActivity)
admin.site.register(ClientActivityAttribute)
admin.site.register(ClientActivityDocument)
admin.site.register(CostCenter)