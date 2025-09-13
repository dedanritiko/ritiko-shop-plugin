"""
Shop Plugin Settings

Defines e-commerce/shop-related settings for organizations using the simplified API.
"""

from core.plugin_organization_settings import create_settings

# Create settings using the simplified API
settings = create_settings("shop_plugin")

# Shop name setting
settings.add_text(
    "shop_name",
    default="My Shop",
    verbose_name="Shop Name",
    help_text="Name of your shop",
    form_section="shop",
)

# Register the settings
settings.register()
