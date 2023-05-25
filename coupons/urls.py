from django.urls import path
from . import views

urlpatterns = [
    path("coupons/", views.CouponView.as_view()),
    path("coupons/<int:coupon_id>/", views.CouponDetailView.as_view()),
]
