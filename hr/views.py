from django.shortcuts import render

from hr.models import Currency, DeductionSalary, DeductionType, Department, Employee, EmployeeDocument,EmployeeJob, EmployeeSalary, VacationRecord, VacationType, WorkingTime
from rest_framework import viewsets , generics
from . import serializer
# Create your views here.

# 1
class EmployeeJobViewset(viewsets.ModelViewSet):
    queryset = EmployeeJob.objects.all()
    serializer_class = serializer.EmployeeJobSerializer

# 2
class DepartmentViewset(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = serializer.DepartmentSerializer

# 3
class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = serializer.EmployeeSerializer

# 4
class EmployeeDocumentViewset(viewsets.ModelViewSet):
    queryset = EmployeeDocument.objects.all()
    serializer_class = serializer.EmployeeDocumentSerializer

# 5
class EmployeeSalaryViewset(viewsets.ModelViewSet):
    queryset = EmployeeSalary.objects.all()
    serializer_class = serializer.EmployeeSalarySerializer

# 6
class DeductionTypeViewset(viewsets.ModelViewSet):
    queryset = DeductionType.objects.all()
    serializer_class = serializer.DeductionTypeSerializer

# 7
class CurrencyViewset(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = serializer.CurrencySerializer

# 8
class DeductionSalaryViewset(viewsets.ModelViewSet):
    queryset = DeductionSalary.objects.all()
    serializer_class = serializer.DeductionSalarySerializer

# 9
class VacationTypeViewset(viewsets.ModelViewSet):
    queryset = VacationType.objects.all()
    serializer_class = serializer.VacationTypeSerializer

# 10
class VacationRecordViewset(viewsets.ModelViewSet):
    queryset = VacationRecord.objects.all()
    serializer_class = serializer.VacationRecordSerializer

# 11
class WorkingTimeViewset(viewsets.ModelViewSet):
    queryset = WorkingTime.objects.all()
    serializer_class = serializer.WorkingTimeSerializer
# ------------------

# 12
class EmployeeJobFilterViewset(viewsets.ModelViewSet):
    queryset = EmployeeJob.objects.filter_by_name('d')
    serializer_class = serializer.EmployeeJobSerializer

# 13
class DepartmentFilterViewset(viewsets.ModelViewSet):
    queryset = Department.objects.filter_by_name('d')
    serializer_class = serializer.DepartmentSerializer


# 14
class EmployeeFilterViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.filter_by_name('d')
    serializer_class = serializer.EmployeeSerializer


class EmpFilter(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = serializer.EmployeeSerializer
    def get_queryset(self):
        return Employee.objects.filter_by_name('l')
