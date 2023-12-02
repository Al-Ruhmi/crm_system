from crm.views import ClientActivityAttributeViewset, ClientActivityDocumentViewset, ClientActivityTypeViewset, ClientActivityViewset, CostCenterFilterViewset, CostCenterViewset, CrmMemberViewset, CrmProjectViewset, CrmTeamFilterViewset, CrmTeamViewset, CustomerAddressViewset, CustomerContractViewset, CustomerCustomFieldViewset, CustomerFilterViewset, CustomerViewset, TaskActivityDocumentViewset, TaskActivityViewset, TaskClassificationViewset, TaskColumnViewset, TaskCommentViewset, TaskCustomFieldViewset, TaskDocumentViewset, TaskHistoryViewset, TaskResponsibleViewset, TaskStatusFilterViewset,CrmProjectFilterViewset, TaskStatusViewset, TaskViewset, TaskWorkLogViewset
from rest_framework import routers

router_crm = routers.DefaultRouter()
# --------------- # ------------------------- Filters Views API Routers
# 1
router_crm.register('customerfilter', CustomerFilterViewset)
# 2
router_crm.register('crmteamfilter', CrmTeamFilterViewset)
# 3
router_crm.register('taskstatusfilter', TaskStatusFilterViewset)
# 4
router_crm.register('crmprojectfilter', CrmProjectFilterViewset)
# 5
router_crm.register('costcenterfilter', CostCenterFilterViewset)

# --------------- # ------------------------- Models Views API Routers

# 1
router_crm.register('customer', CustomerViewset)
# 2
router_crm.register('customeraddress', CustomerAddressViewset)
# 3
router_crm.register('customercustomfield', CustomerCustomFieldViewset)
# 4
router_crm.register('customercontract', CustomerContractViewset)
# 5
router_crm.register('crmteam', CrmTeamViewset)
# 6
router_crm.register('crmmember', CrmMemberViewset)
# 7
router_crm.register('taskstatus', TaskStatusViewset)
# 8
router_crm.register('taskclassification', TaskClassificationViewset)
# 9
router_crm.register('taskcustomfield', TaskCustomFieldViewset)
# 10
router_crm.register('crmproject', CrmProjectViewset)
# 11
router_crm.register('task', TaskViewset)
# 12
router_crm.register('taskdocument', TaskDocumentViewset)
# 13
router_crm.register('taskactivity', TaskActivityViewset)
# 14
router_crm.register('taskactivitydocument', TaskActivityDocumentViewset)
# 15
router_crm.register('taskresponsible', TaskResponsibleViewset)
# 16
router_crm.register('taskcomment', TaskCommentViewset)
# 17
router_crm.register('taskworklog', TaskWorkLogViewset)
# 18
router_crm.register('taskcolumn', TaskColumnViewset)
# 19
router_crm.register('taskhistory', TaskHistoryViewset)
# 20
router_crm.register('clientactivitytype', ClientActivityTypeViewset)
# 21
router_crm.register('clientactivity', ClientActivityViewset)
# 22
router_crm.register('clientactivityattribute', ClientActivityAttributeViewset)
# 23
router_crm.register('clientactivitydocument', ClientActivityDocumentViewset)
# 23
router_crm.register('costcenter', CostCenterViewset)

