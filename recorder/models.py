from django.db import models
from django.contrib.auth.models import User  # Django's User

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    class Meta:
        db_table = 'user_profiles'

class Song(models.Model):
    name = models.CharField(max_length=200)
    original_file = models.FileField(upload_to='songs/')
    accompaniment_file = models.FileField(upload_to='songs/')
    lyrics_image = models.ImageField(upload_to='lyrics_images/', blank=True, null=True)
    uploaded_by = models.CharField(max_length=50, default='admin')
    created_at = models.DateTimeField(auto_now_add=True)
    is_shared = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Recording(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    file = models.FileField(upload_to='recordings/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} - {self.song.name}"
