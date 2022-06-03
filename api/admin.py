from django.contrib import admin
from .models import Squad


# Register your models here.
@admin.register(Squad)
class SquadAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'members', 'color']
