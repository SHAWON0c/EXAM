# from django.shortcuts import render , redirect
# from .import forms
# from . import models
# from django.contrib.auth.decorators import login_required
# def musician(request):
#      if request.method == 'POST':
#          musician_form=forms.MusicianForm(request.POST)
#          if musician_form.is_valid():
#               musician_form.save()
#               return redirect('homepage')
#      else:
#           musician_form=forms.MusicianForm()
          
#      return render(request, 'musician.html', {'form': musician_form})
# @login_required
# def edit_musician(request , id ):
#      musician = models.Musician.objects.get(pk=id)
#      musician_form=forms.MusicianForm(instance=musician)
#      if request.method == 'POST':
#          musician_form=forms.MusicianForm(request.POST ,instance=musician)
#          if musician_form.is_valid():
#               musician_form.save()
#               return redirect('homepage')

          
#      return render(request, 'musician.html', {'form': musician_form})


# @login_required
# def delete_musician(request , id ):
#      musician = models.Musician.objects.get(pk=id)
#      musician.delete()
#      return redirect('homepage')



from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import forms, models

class MusicianCreateView(LoginRequiredMixin, CreateView):
    template_name = 'musician.html'
    form_class = forms.MusicianForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MusicianUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'musician.html'
    form_class = forms.MusicianForm
    success_url = reverse_lazy('homepage')
    queryset = models.Musician.objects.all()

class MusicianDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Musician
    success_url = reverse_lazy('homepage')
