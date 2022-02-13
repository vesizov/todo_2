from django.contrib import admin
from .models import Todo

class Todo_admin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todo, Todo_admin)

