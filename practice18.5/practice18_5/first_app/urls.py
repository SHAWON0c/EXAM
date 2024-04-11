from django.urls import path
from . import views

urlpatterns = [
    # path('', views.<view_function_name>, name='homepage')
    path('signup/', views.Signup, name='signup'),
    path('login/', views.login_view, name='login'),  # Changed the name of the view function
    path('profile/', views.profile, name='profile'),  # Corrected the typo in 'name'
    path('logout/',views.logout_view, name='logout'),
    path('changepass/',views.changepass, name='changepass'),
    path('changepass2/',views.changepass2, name='changepass2'),
]
