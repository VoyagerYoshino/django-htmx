from django.contrib import admin
from .models import Film,UserFilm
# Register your models here.

admin.site.register(Film)
admin.site.register(UserFilm)