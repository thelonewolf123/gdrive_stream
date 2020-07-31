from django.shortcuts import render
from django.http import StreamingHttpResponse
from .models import Gdrive
from .helper import download_file_from_google_drive

def single_video(request):

    return render(request,'streamd/single-video.html')

def video_stream(request,id):

    gdrive = Gdrive.objects.get(pk=id)
    gdrive_response = download_file_from_google_drive(gdrive.gdrive_link)
    return StreamingHttpResponse(streaming_content=gdrive_response.raw)

def video_list(request):

    gdrive = Gdrive.objects.all()
    context= {}
    context['gdrive'] = gdrive
    return render(request,'streamd/video-list.html',context=gdrive)