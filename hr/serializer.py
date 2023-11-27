from rest_framework import serializers
from .models import Currency, DeductionSalary, DeductionType, EmployeeDocument,Department, Employee,EmployeeJob, EmployeeSalary, VacationRecord, VacationType, WorkingTime


# 1
class EmployeeJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeJob
        fields = '__all__'

# 2
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

# 3
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

# 4
class EmployeeDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDocument
        fields = '__all__'

# 5
class EmployeeSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSalary
        fields = '__all__'

# 6
class DeductionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeductionType
        fields = '__all__'

# 7
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

# 8
class DeductionSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeductionSalary
        fields = '__all__'

# 9
class VacationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacationType
        fields = '__all__'

# 10
class VacationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacationRecord
        fields = '__all__'

# 11
class WorkingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingTime
        fields = '__all__'