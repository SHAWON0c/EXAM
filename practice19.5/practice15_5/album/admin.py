# from django.contrib import admin
# from .models import Musician

# class MusicianAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email', 'phone_number', 'instrument_type')
#     search_fields = ['first_name', 'last_name', 'email', 'phone_number', 'instrument_type']

# admin.site.register(Musician, MusicianAdmin)


from django.contrib import admin
from .models import Album

class Albumadmin(admin.ModelAdmin):
    list_display = [field.name for field in Album._meta.fields]

admin.site.register(Album, Albumadmin)
