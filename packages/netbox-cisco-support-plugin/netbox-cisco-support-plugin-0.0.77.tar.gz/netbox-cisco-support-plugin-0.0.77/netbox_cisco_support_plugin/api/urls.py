from netbox.api.routers import NetBoxRouter
from . import views


app_name = "netbox_cisco_support_plugin"

router = NetBoxRouter()
# Cisco Support
router.register(r"device", views.CiscoDeviceSupportViewSet)
router.register(r"device-type", views.CiscoDeviceTypeSupportViewSet)
# Fortnet Support
router.register(r"fortinet", views.FortinetSupportViewSet)

urlpatterns = router.urls
