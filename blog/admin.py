from django.contrib import admin
from .models import Post
# Register your models here.

''' Para hacer nuestro modelo visible en la pagina del administrador'''
admin.site.register(Post)
