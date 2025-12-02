from django.db import models

class UploadedSong(models.Model):
    title = models.CharField(max_length=200, blank=True)

    original_file = models.FileField(upload_to='songs/originals/')
    accompaniment_file = models.FileField(upload_to='songs/accompaniments/', null=True, blank=True)

    lyrics_image = models.ImageField(upload_to='songs/lyrics_images/', null=True, blank=True)
    lyrics = models.TextField(blank=True)

    is_instrumental = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or self.original_file.name
