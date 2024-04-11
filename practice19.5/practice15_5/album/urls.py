# from django.urls import path
# from .import views

# urlpatterns = [
#     path('add/',views.album , name='album'),
#     path('edit/<int:id>', views.edit_album, name='edit_album')
    
# ]


from django.urls import path
from .views import AlbumCreateView, AlbumUpdateView, AlbumDeleteView

urlpatterns = [
    path('album/', AlbumCreateView.as_view(), name='album'),
    path('album/edit/<int:pk>/', AlbumUpdateView.as_view(), name='edit_album'),
    path('album/delete/<int:pk>/', AlbumDeleteView.as_view(), name=''),
]
