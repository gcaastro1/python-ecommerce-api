from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductView.as_view()),
    path("products/<int:product_id>/", views.ProductDetailView.as_view()),
    path("products/<int:product_id>/comments/", views.ProductCommentsView.as_view()),
    path(
        "products/comments/<int:comment_id>/", views.ProductCommentsDetailView.as_view()
    ),
]
