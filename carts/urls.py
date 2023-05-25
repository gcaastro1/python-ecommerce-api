from django.urls import path
from . import views
from carts_products import views as cp_views

urlpatterns = [
    path("cart/", views.CartView.as_view()),
    path("cart/product/", cp_views.CartProductView.as_view()),
    path("cart/product/<int:pk>/", cp_views.CartProductDetailView.as_view()),
]
