from django.urls import path
from . import views

urlpatterns = [

    path('buy_now/<int:car_id>/', views.buy_now, name='buy_now'),
    path('car_details/<int:car_id>/', views.car_details, name='cardetails')
    
]
