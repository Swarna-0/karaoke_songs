from django.contrib import admin
from .models import UploadedSong

@admin.register(UploadedSong)
class UploadedSongAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_instrumental', 'created_at', 'original_file', 'accompaniment_file')
    readonly_fields = ('created_at',)
