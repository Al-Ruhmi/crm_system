from django.contrib import admin

# Register your models here.
from .models import  MenuGroup,Menu,WidgetGroup,Widget,WidgetConfig,Settings



admin.site.register(MenuGroup)
admin.site.register(Menu)
admin.site.register(WidgetGroup)
admin.site.register(Widget)
admin.site.register(WidgetConfig)
admin.site.register(Settings)