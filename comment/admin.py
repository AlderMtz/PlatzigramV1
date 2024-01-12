from django.contrib import admin
from comment.models import Comment

# Register your models here.
@admin.register(Comment)
class ProfileAdmin(admin.ModelAdmin): # Damos de alta al modelo llamado "Comment" para poder verlo en el ADMIN.
    """Comment admin."""
    list_display = ('pk','user','post','body','date') # Modificamos la forma en que ADMIN mostraran los datos.
    search_fields = ('user','date') # Declaramos campos que se podra buscar.
    list_filter = (
        'user',
        'date'
    ) 
