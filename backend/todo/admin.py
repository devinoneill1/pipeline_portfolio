from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'createdDTF', 'completedDTF')

# Register your models here.

admin.site.register(Todo, TodoAdmin)