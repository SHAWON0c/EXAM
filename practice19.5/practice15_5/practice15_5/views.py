from django.shortcuts import render
from album.models import Album
from musician.models import Musician

# def home(request):
#     albums = Album.objects.all()
#     musicians = Musician.objects.all()

#     # Combine data from both models into a single list
#     combined_data = [{'album': album, 'musician': musician} for album, musician in zip(albums, musicians)]

#     return render(request, 'home.html', {'combined_data': combined_data})


from django.views.generic import ListView

class HomeView(ListView):
    template_name = 'home.html'
    context_object_name = 'combined_data'
    queryset = None

    def get_queryset(self):
        albums = Album.objects.all()
        musicians = Musician.objects.all()
        
        combined_data = [{'album': album, 'musician': musician} for album, musician in zip(albums, musicians)]
        return combined_data
