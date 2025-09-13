"""
Shop Plugin Widgets
Registers widgets for the shop plugin to be displayed in various zones.
"""
from core.plugin_widgets import Widget, plugin_widget_registry


def check_shop_permissions(request):
    """Check if user has shop management permissions."""
    if not request or not hasattr(request, "user"):
        return False
    # Check if user is superadmin or has shop permissions
    user = request.user
    if hasattr(user, "is_superadmin") and user.is_superadmin:
        return True
    if hasattr(user, "user_type") and user.user_type == "SADM":  # Super Admin user type
        return True
    return False


def get_products_context(request):
    """Context processor for products widget."""
    from .models import Product

    # Get active products
    products = Product.objects.filter(is_active=True)[:5]

    return {
        "products": products,
    }


# Register shop widgets
plugin_widget_registry.register_widget(
    widget=Widget(
        name="shop_products",
        plugin_id="shop_plugin",
        template="shop_plugin/widgets/products.html",
        context_processor=get_products_context,
        zone_compatible=["dashboard_medium"],
        priority=6,
        width_classes="col-md-8",
        permissions=["shop_plugin.can_view_shop"],
        conditions=check_shop_permissions,
        css_classes="shop-widget products-widget",
    ),
    zones=["dashboard_medium"],
)
