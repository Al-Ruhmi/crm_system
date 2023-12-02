from rest_framework import serializers
from .models import ClientActivity, ClientActivityAttribute, ClientActivityDocument, ClientActivityType, CostCenter,TaskStatus, Customer,CrmTeam, Task, TaskActivity, TaskActivityDocument, TaskClassification, TaskColumn, TaskComment, TaskCustomField, TaskDocument, TaskHistory, TaskResponsible,TaskStatus,CrmProject,CustomerAddress,CustomerCustomField,CustomerContract,CrmMember, TaskWorkLog

# 1
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

# 2
class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = '__all__'

# 3
class CustomerCustomFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCustomField
        fields = '__all__'

# 4
class CustomerContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerContract
        fields = '__all__'

# 5
class CrmTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrmTeam
        fields = '__all__'

# 6
class CrmMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrmMember
        fields = '__all__'

# 7
class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = '__all__'

# 8
class TaskClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskClassification
        fields = '__all__'

# 9
class TaskCustomFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCustomField
        fields = '__all__'

# 10
class CrmProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrmProject
        fields = '__all__'

# 11
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

# 12
class TaskDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDocument
        fields = '__all__'

# 13
class TaskActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskActivity
        fields = '__all__'

# 14
class TaskActivityDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskActivityDocument
        fields = '__all__'

# 15
class TaskResponsibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskResponsible
        fields = '__all__'

# 16
class TaskCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = '__all__'

# 17
class TaskWorkLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskWorkLog
        fields = '__all__'

# 18
class TaskColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskColumn
        fields = '__all__'

# 19
class TaskHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskHistory
        fields = '__all__'

# 20
class ClientActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientActivityType
        fields = '__all__'

# 21
class ClientActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientActivity
        fields = '__all__'

# 22
class ClientActivityAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientActivityAttribute
        fields = '__all__'

# 23
class ClientActivityDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientActivityDocument
        fields = '__all__'

# 24
class CostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenter
        fields = '__all__'