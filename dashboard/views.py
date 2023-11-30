from django.shortcuts import render
from .models import MenuGroup,Menu,WidgetGroup,Widget,WidgetConfig,Settings
from rest_framework import viewsets 
from . import serializer

# Create your views here.

# ------------------------- Filters Manager API
# 1.1
class MenuGroupFilterViewset(viewsets.ModelViewSet):
    queryset = MenuGroup.objects.filter_by_name('m')
    serializer_class = serializer.MenuGroupSerializer

# 2.1
class MenuFilterViewset(viewsets.ModelViewSet):
    queryset = Menu.objects.filter_by_name('m')
    serializer_class = serializer.MenuSerializer

# 3.1
class WidgetGroupFilterViewset(viewsets.ModelViewSet):
    queryset = WidgetGroup.objects.filter_by_name('m')
    serializer_class = serializer.WidgetGroupSerializer

# 4.1
class WidgetFilterViewset(viewsets.ModelViewSet):
    queryset = Widget.objects.filter_by_name('m')
    serializer_class = serializer.WidgetSerializer

# 5.1
class WidgetConfigFilterViewset(viewsets.ModelViewSet):
    queryset = WidgetConfig.objects.filter_by_name('m')
    serializer_class = serializer.WidgetConfigSerializer

# 6.1
class SettingsFilterViewset(viewsets.ModelViewSet):
    queryset = Settings.objects.filter_by_name('m')
    serializer_class = serializer.SettingsSerializer


# ------------------------- Models Views API
# 1.2
class MenuGroupViewset(viewsets.ModelViewSet):
    queryset = MenuGroup.objects.all()
    serializer_class = serializer.MenuGroupSerializer

# 2.2
class MenuViewset(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = serializer.MenuSerializer

# 3.2
class WidgetGroupViewset(viewsets.ModelViewSet):
    queryset = WidgetGroup.objects.all()
    serializer_class = serializer.WidgetGroupSerializer

# 4.2
class WidgetViewset(viewsets.ModelViewSet):
    queryset = Widget.objects.all()
    serializer_class = serializer.WidgetSerializer

# 5.2
class WidgetConfigViewset(viewsets.ModelViewSet):
    queryset = WidgetConfig.objects.all()
    serializer_class = serializer.WidgetConfigSerializer

# 1.2
class SettingsViewset(viewsets.ModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = serializer.SettingsSerializer