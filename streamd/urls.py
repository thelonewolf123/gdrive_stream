from django.urls import path
from . import views

urlpatterns = [
    path('video/<uuid:public_id>',views.single_video,name='single_video'),
    path('',views.video_list,name='video_list'),
    path('video/<int:id>',views.video_stream,name='video_stream')
]