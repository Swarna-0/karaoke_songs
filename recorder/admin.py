from django.contrib import admin
from .models import Song, UserProfile, Recording  # ← REMOVED User

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['name', 'uploaded_by', 'is_shared', 'created_at']
    list_filter = ['is_shared', 'created_at']
    search_fields = ['name']

@admin.register(UserProfile)  # ✅ ADD UserProfile
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role']
    list_filter = ['role']

@admin.register(Recording)
class RecordingAdmin(admin.ModelAdmin):
    list_display = ['song', 'user', 'created_at']
    list_filter = ['created_at']
