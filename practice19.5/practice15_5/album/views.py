# from django.shortcuts import render , redirect
# from .import forms
# from . import models
# from django.contrib.auth.decorators import login_required
# # Create your views here.
# def album(request):
#      if request.method == 'POST':
#          album_form=forms.AlbumForm(request.POST)
#          if album_form.is_valid():
#               album_form.save()
#               return redirect('homepage')
#      else:
#           album_form=forms.AlbumForm()
          
#      return render(request, 'album.html', {'form': album_form})
# @login_required
# def edit_album(request , id ):
#      album = models.Album.objects.get(pk=id)
#      album_form=forms.AlbumForm(instance=album)
#      if request.method == 'POST':
#          album_form=forms.AlbumForm(request.POST ,instance=album)
#          if album_form.is_valid():
#               album_form.save()
#               return redirect('homepage')

          
#      return render(request, 'album.html', {'form': album_form})

# @login_required
# def delete_album(request):
#      album = models.Album.objects.get(pk=id)
#      album.delete()
#      return redirect('homepage')




from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import forms, models

class AlbumCreateView(LoginRequiredMixin, CreateView):
    template_name = 'album.html'
    form_class = forms.AlbumForm
    success_url = reverse_lazy('homepage')

class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'album.html'
    form_class = forms.AlbumForm
    success_url = reverse_lazy('homepage')
    queryset = models.Album.objects.all()

class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Album
    success_url = reverse_lazy('homepage')
