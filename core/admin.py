
from django.contrib import admin
from .models import BusinessType,Company,CustomFieldType,CustomField


# Register your models here.


admin.site.register(BusinessType)
admin.site.register(Company)
admin.site.register(CustomFieldType)
admin.site.register(CustomField)
