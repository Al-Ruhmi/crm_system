
from django.contrib import admin

# Register your models here.
from .models import EmployeeJob,Department,Employee,EmployeeDocument,DeductionType,Currency,DeductionSalary,VacationRecord,WorkingTime
# Register your models here.



admin.site.register(WorkingTime)
admin.site.register(VacationRecord)
admin.site.register(DeductionSalary)
admin.site.register(Currency)
admin.site.register(DeductionType)
admin.site.register(EmployeeDocument)
admin.site.register(Employee)
admin.site.register(EmployeeJob)
admin.site.register(Department)