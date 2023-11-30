from rest_framework import serializers
from .models import MenuGroup,Menu,WidgetGroup,Widget,WidgetConfig,Settings

# 1
class MenuGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuGroup
        fields = '__all__'

# 2
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

# 3
class WidgetGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = WidgetGroup
        fields = '__all__'

# 4
class WidgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Widget
        fields = '__all__'

# 5
class WidgetConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = WidgetConfig
        fields = '__all__'

# 6
class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'