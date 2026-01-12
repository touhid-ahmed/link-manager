from django.contrib import admin

# Register your models here.
from .models import Link



@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'link_url', 'description','created', 'updated']