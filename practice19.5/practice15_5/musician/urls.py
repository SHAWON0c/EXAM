# from django.urls import path,include
# from . import views 

# urlpatterns = [
#     path('add/',views.musician , name ='musician'),
#     path('edit/<int:id>',views.edit_musician,name='edit_musician'),
#     path('delete/<int:id>', views.delete_musician, name='dlt_musician')
# ]



from django.urls import path
from .views import MusicianCreateView, MusicianUpdateView, MusicianDeleteView

urlpatterns = [
    path('musician/', MusicianCreateView.as_view(), name='musician'),
    path('musician/edit/<int:pk>/', MusicianUpdateView.as_view(), name='edit_musician'),
    path('musician/delete/<int:pk>/', MusicianDeleteView.as_view(), name='dlt_musician'),
]
