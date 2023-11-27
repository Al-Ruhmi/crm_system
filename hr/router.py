from hr.views import CurrencyViewset, DeductionSalaryViewset, DeductionTypeViewset, DepartmentFilterViewset, DepartmentViewset, EmpFilter, EmployeeDocumentViewset, EmployeeJobFilterViewset, EmployeeJobViewset, EmployeeSalaryViewset, EmployeeViewset,EmployeeFilterViewset, VacationRecordViewset, VacationTypeViewset, WorkingTimeViewset
from rest_framework import routers

router = routers.DefaultRouter()
# 1
router.register('employeejob', EmployeeJobViewset)
# 2
router.register('department', DepartmentViewset)
# 3
router.register('employee', EmployeeViewset)
# 4
router.register('employeedocument', EmployeeDocumentViewset)
# 5
router.register('employeesalary', EmployeeSalaryViewset)
# 6
router.register('deductiontype', DeductionTypeViewset)
# 7
router.register('currency', CurrencyViewset)
# 8
router.register('deductionsalary', DeductionSalaryViewset)
# 9
router.register('vacationtype', VacationTypeViewset)
# 10
router.register('vacationrecord', VacationRecordViewset)
# 11
router.register('workingtime', WorkingTimeViewset)
# ------------------
# 12
router.register('empjobfilter', EmployeeJobFilterViewset)
# 13
router.register('depfilter', DepartmentFilterViewset)
# 14
router.register('empfilter', EmployeeFilterViewset)