"""
Shop Plugin Permissions

Defines custom permissions for the e-commerce shop plugin using the simplified API.
"""
from core.plugin_permissions import create_permissions

# Create permissions using the simplified API
permissions = create_permissions("shop_plugin")

# Shop view permission
permissions.add_permission(
    codename="can_view_shop",
    name="Can view shop",
    description="Permission to view the shop",
    category="shop",
)

# Register the permissions
permissions.register()
