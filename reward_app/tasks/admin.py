from django.contrib import admin
from .models import App, Task

# Optionally, create a custom ModelAdmin class for more control over the admin interface

class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'app', 'is_completed', 'screenshot')
    list_filter = ('is_completed', 'user', 'app')  # Filters in the sidebar
    search_fields = ('user__username', 'app__name')  # Search by user or app name
    
class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'points')
    search_fields = ('name',)  # Search by app name
    list_filter = ('points',)  # You can add filters for the points field if needed

# Register models in the admin
admin.site.register(App, AppAdmin)
admin.site.register(Task, TaskAdmin)
