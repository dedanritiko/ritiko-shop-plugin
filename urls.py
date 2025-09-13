from django.urls import path

from . import views

app_name = "shop_plugin"

urlpatterns = [
    path("", views.shop_view, name="shop"),
    path("product/<int:product_id>/", views.product_detail, name="product_detail"),
]
