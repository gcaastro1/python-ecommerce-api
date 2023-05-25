from django.urls import path
from .views import WishListView, WishListAddView, WishListRemoveView


urlpatterns = [
    path("wishlist/", WishListView.as_view()),
    path("wishlist/add/<int:product_id>/", WishListAddView.as_view()),
    path("wishlist/remove/<int:product_id>/", WishListRemoveView.as_view()),
]
