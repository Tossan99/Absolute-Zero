from django.urls import path
from . import views


urlpatterns = [
    path("", views.view_profile, name="profile"),
    path("order_history/<order_number>", views.view_order_history, name="order_history"),
    
]