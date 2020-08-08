from django.urls import path
from . import views

urlpatterns = [
    path('',views.video_list,name='video_list'),
    path('video/<int:id>',views.single_video,name='video_stream')
]