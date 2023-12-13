from django.contrib import admin
from blog.models import DressingRooms, Blog
# Register your models here.

@admin.register(DressingRooms)
class Dressing(admin.ModelAdmin):
    list_display = ['id', 'floor', 'numbers']
    ordering = ['id']

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'age', 'email', 'created_at', 'dressing']
    list_editable = ['dressing']
    ordering = ['id']