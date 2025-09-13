"""
Shop Plugin Menu Items

Defines menu items for the e-commerce shop plugin using the simplified API.
"""
from core.plugin_menus import create_menu

# Create shop menu using the simplified API
menu = create_menu("shop_plugin", section="commerce")

# Add standalone menu item
menu.add_item(
    name="Shop",
    url_name="shop_plugin:shop",
    icon="fas fa-store",
    order=10,
    tooltip="View shop",
)

# Register the menu
menu.register()
