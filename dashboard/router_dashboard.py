from dashboard.views import MenuFilterViewset, MenuGroupFilterViewset, MenuGroupViewset, MenuViewset, SettingsFilterViewset, SettingsViewset, WidgetConfigFilterViewset, WidgetConfigViewset, WidgetFilterViewset, WidgetGroupFilterViewset, WidgetGroupViewset, WidgetViewset 
from rest_framework import routers

router_dashboard = routers.DefaultRouter()
# --------------- # ------------------------- Filters Views API Routers
# 1.1
router_dashboard.register('menugroupfilter', MenuGroupFilterViewset)
# 2.1
router_dashboard.register('menufilter', MenuFilterViewset)
# 3.1
router_dashboard.register('widgetgroupfilter', WidgetGroupFilterViewset)
# 4.1
router_dashboard.register('widgetfilter', WidgetFilterViewset)
# 5.1
router_dashboard.register('widgetconfigfilter', WidgetConfigFilterViewset)
# 6.1
router_dashboard.register('settingsfilter', SettingsFilterViewset)

# --------------- # ------------------------- Models Views API Routers

# 1.2
router_dashboard.register('menugroup', MenuGroupViewset)
# 2.2
router_dashboard.register('menu', MenuViewset)
# 3.2
router_dashboard.register('widgetgroup', WidgetGroupViewset)
# 4.2
router_dashboard.register('widget', WidgetViewset)
# 5.2
router_dashboard.register('widgetconfig', WidgetConfigViewset)
# 6.2
router_dashboard.register('settings', SettingsViewset)