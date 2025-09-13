from core.plugin_app_config import PluginAppConfig


class ShopPluginConfig(PluginAppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "plugins.shop_plugin"
    verbose_name = "Shop Plugin"
