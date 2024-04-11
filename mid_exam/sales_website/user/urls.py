from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('signup/', views.signup.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
     path('logout/', views.logout_view, name='logout'),
     path('edit/', views.EditUserView.as_view(), name='edit_user'),
]
