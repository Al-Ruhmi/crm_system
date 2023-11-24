from django.db import models
# from dashboard.enums import WidgetType

from core.models import AddOn, BaseModel, BaseModelWithAuthor, CustomFieldType
from django.utils.translation import gettext_lazy as _
# Create your models here.

class MenuGroup(BaseModel):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True,blank=True)
    position = models.IntegerField(null=True , blank=True)
    active = models.BooleanField(default=True)

class Menu(BaseModel):
    name = models.CharField(max_length=255, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    group = models.ForeignKey(MenuGroup, null=True, blank=True, on_delete=models.CASCADE)
    model = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=255, null=True)
    position = models.IntegerField(null=True , blank=True)
    active = models.BooleanField(default=True)


class WidgetGroup(BaseModel):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True,blank=True)
    position = models.IntegerField(null=True , blank=True)
    active = models.BooleanField(default=True)


# enum task

class Widget(BaseModel):
    class WidgetType(models.TextChoices):
        
        CARD = 'CR', _('Card')
        GRAPHIC = 'GR', _('Graphic')
        TABLE = 'TB', _('Table')

    name = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
    info = models.TextField(null=True,blank=True)
    type = models.CharField(max_length=255, choices=WidgetType.choices)
    group = models.ForeignKey(WidgetGroup, null=True, blank=True, on_delete=models.CASCADE)
    url_view = models.CharField(max_length=255, null=True)
    url_api = models.CharField(max_length=255, null=True)
    width = models.IntegerField(null=True , blank=True)
    height = models.IntegerField(null=True , blank=True)
    position = models.IntegerField(null=True , blank=True)
    active = models.BooleanField(default=True)

class WidgetConfig(BaseModel):
    name = models.CharField(max_length=255, null=True)
    widget = models.ForeignKey(Widget, null=True, blank=True, on_delete=models.CASCADE)
    type = models.ForeignKey(CustomFieldType, null=True, blank=True, on_delete=models.CASCADE)
    value = models.CharField(max_length=255, null=True)

class Settings(BaseModelWithAuthor):
    name = models.CharField(max_length=255, null=True)
    addon = models.ForeignKey(AddOn, null=True, blank=True, on_delete=models.CASCADE)
    model = models.CharField(max_length=255, null=True)
    type = models.ForeignKey(CustomFieldType, null=True, blank=True, on_delete=models.CASCADE)
    object_type = models.CharField(max_length=255, null=True)
    value = models.CharField(max_length=255, null=True)
    default_value = models.CharField(max_length=255, null=True)
    active = models.BooleanField(default=True)






