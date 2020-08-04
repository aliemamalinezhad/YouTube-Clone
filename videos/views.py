from django.shortcuts import render, get_object_or_404
from .models import Video
from .forms import VideoForm


# Create your views here.
def dashboard(request):
    videos = Video.objects.all()
    # path = video.path

    # form = VideoForm(request.POST or None, request.FILES or None)
    # if form.is_valid():
    #     form.save()

    context = {
        'videos': videos,
        # 'form': form,
    }
    return render(request, 'videos/dashboard.html', context)

def get_video(request,video_id):
    video = get_object_or_404(Video, pk=video_id)
    context = {
        'video': video
    }
    return render(request, 'videos/video.html', context)

def admin_panel(request):
    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {

        'form': form,
    }
    return render(request, 'videos/admin_panel.html', context)
