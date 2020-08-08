from django.shortcuts import render
from django.http import StreamingHttpResponse
from .models import Gdrive
from django.conf import settings

def single_video(request,id):
    gdrive = Gdrive.objects.get(pk=id)
    file_id = gdrive.gdrive_link.split('/')[5]
    context = {}
    context['file_id'] = file_id
    context['api_key'] = settings.API_KEY
    context['title'] = gdrive.title
    context['discription'] = gdrive.discription
    return render(request,'streamd/single-video.html',context=context)

def video_list(request):
    gdrive = Gdrive.objects.all()
    context= {}
    context['gdrive'] = gdrive
    return render(request,'streamd/video-list.html',context=context)