from django.urls import path
from . import views

app_name = 'recorder'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_recording/<int:song_id>/', views.upload_recording, name='upload_recording'),
]
