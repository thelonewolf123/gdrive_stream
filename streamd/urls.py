from django.urls import path
from . import views

urlpatterns = [
    path('video/<int:id>',views.single_video,name='video-list'),
    path('',views.video_list,name='video_list'),
    path('video-stream/<int:id>',views.video_stream,name='video_stream')
]