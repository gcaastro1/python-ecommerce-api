from django.urls import path
from . import views

urlpatterns = [
    path("users/<int:user_id>/addresses/", views.AddressView.as_view()),
    path("users/<int:user_id>/addresses/<int:pk>/", views.AddressDetailView.as_view()),
]
