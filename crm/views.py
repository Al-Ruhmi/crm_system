from django.shortcuts import render
from .models import ClientActivity, ClientActivityAttribute, ClientActivityDocument, ClientActivityType,TaskStatus, Customer,CrmTeam, Task, TaskActivity, TaskActivityDocument, TaskClassification, TaskColumn, TaskComment, TaskCustomField, TaskDocument, TaskHistory, TaskResponsible,TaskStatus,CrmProject,CustomerAddress,CustomerCustomField,CustomerContract,CrmMember, TaskWorkLog
from rest_framework import viewsets 
from . import serializer

# Create your views here.

# ------------------------- Filters Manager API
# 1
class CustomerFilterViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.filter_by_basic(True)
    serializer_class = serializer.CustomerSerializer

# 2
class CrmTeamFilterViewset(viewsets.ModelViewSet):
    queryset = CrmTeam.objects.filter_by_name('f')
    serializer_class = serializer.CrmTeamSerializer

# 3
class TaskStatusFilterViewset(viewsets.ModelViewSet):
    queryset = TaskStatus.objects.filter_by_name('d')
    serializer_class = serializer.TaskStatusSerializer

# 4
class CrmProjectFilterViewset(viewsets.ModelViewSet):
    queryset = CrmProject.objects.filter_by_name('d')
    serializer_class = serializer.CrmProjectSerializer

# ------------------------- Models Views API
# 1
class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = serializer.CustomerSerializer

# 2
class CustomerAddressViewset(viewsets.ModelViewSet):
    queryset = CustomerAddress.objects.all()
    serializer_class = serializer.CustomerAddressSerializer

# 3
class CustomerCustomFieldViewset(viewsets.ModelViewSet):
    queryset = CustomerCustomField.objects.all()
    serializer_class = serializer.CustomerCustomFieldSerializer

# 4
class CustomerContractViewset(viewsets.ModelViewSet):
    queryset = CustomerContract.objects.all()
    serializer_class = serializer.CustomerContractSerializer

# 5
class CrmTeamViewset(viewsets.ModelViewSet):
    queryset = CrmTeam.objects.all()
    serializer_class = serializer.CrmTeamSerializer

# 6
class CrmMemberViewset(viewsets.ModelViewSet):
    queryset = CrmMember.objects.all()
    serializer_class = serializer.CrmMemberSerializer

# 7
class TaskStatusViewset(viewsets.ModelViewSet):
    queryset = TaskStatus.objects.all()
    serializer_class = serializer.TaskStatusSerializer

# 8
class TaskClassificationViewset(viewsets.ModelViewSet):
    queryset = TaskClassification.objects.all()
    serializer_class = serializer.TaskClassificationSerializer

# 9
class TaskCustomFieldViewset(viewsets.ModelViewSet):
    queryset = TaskCustomField.objects.all()
    serializer_class = serializer.TaskCustomFieldSerializer

# 10
class CrmProjectViewset(viewsets.ModelViewSet):
    queryset = CrmProject.objects.all()
    serializer_class = serializer.CrmProjectSerializer

# 11
class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = serializer.TaskSerializer

# 12
class TaskDocumentViewset(viewsets.ModelViewSet):
    queryset = TaskDocument.objects.all()
    serializer_class = serializer.TaskDocumentSerializer

# 13
class TaskActivityViewset(viewsets.ModelViewSet):
    queryset = TaskActivity.objects.all()
    serializer_class = serializer.TaskActivitySerializer

# 14
class TaskActivityDocumentViewset(viewsets.ModelViewSet):
    queryset = TaskActivityDocument.objects.all()
    serializer_class = serializer.TaskActivityDocumentSerializer

# 15
class TaskResponsibleViewset(viewsets.ModelViewSet):
    queryset = TaskResponsible.objects.all()
    serializer_class = serializer.TaskResponsibleSerializer

# 16
class TaskCommentViewset(viewsets.ModelViewSet):
    queryset = TaskComment.objects.all()
    serializer_class = serializer.TaskCommentSerializer

# 17
class TaskWorkLogViewset(viewsets.ModelViewSet):
    queryset = TaskWorkLog.objects.all()
    serializer_class = serializer.TaskWorkLogSerializer

# 18
class TaskColumnViewset(viewsets.ModelViewSet):
    queryset = TaskColumn.objects.all()
    serializer_class = serializer.TaskColumnSerializer

# 19
class TaskHistoryViewset(viewsets.ModelViewSet):
    queryset = TaskHistory.objects.all()
    serializer_class = serializer.TaskHistorySerializer

# 20
class ClientActivityTypeViewset(viewsets.ModelViewSet):
    queryset = ClientActivityType.objects.all()
    serializer_class = serializer.ClientActivityTypeSerializer

# 21
class ClientActivityViewset(viewsets.ModelViewSet):
    queryset = ClientActivity.objects.all()
    serializer_class = serializer.ClientActivitySerializer

# 22
class ClientActivityAttributeViewset(viewsets.ModelViewSet):
    queryset = ClientActivityAttribute.objects.all()
    serializer_class = serializer.ClientActivityAttributeSerializer

# 23
class ClientActivityDocumentViewset(viewsets.ModelViewSet):
    queryset = ClientActivityDocument.objects.all()
    serializer_class = serializer.ClientActivityDocumentSerializer
