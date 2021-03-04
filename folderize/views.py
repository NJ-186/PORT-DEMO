from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Video, Folder
from .forms import VideoForm, FolderForm

import json

# Create your views here.

@login_required
def main(request):
    videos = {}

    folders = Folder.objects.filter(user = request.user)

    for folder in folders:
        video_queryset = Video.objects.filter(folder = folder, user = request.user)
        videos[folder.title] = [v.title for v in video_queryset]

    videos['No Folder Assigned'] = [v.title for v in Video.objects.filter(folder = None, user = request.user)]

    return render(request, 'folderize/main.html', {
        'videos' : json.dumps(videos),
    })


@login_required
def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request, request.POST) # sending 'request' to check the type of request made
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user  # saving user
            video.save()
            return redirect('main')

    else:
        form = VideoForm(request)

    return render(request, 'folderize/add_video.html', {
        'form' : form
    })


@login_required
def add_folder(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.user = request.user  # saving user
            folder.save()
            return redirect('main')

    else:
        form = FolderForm()

    return render(request, 'folderize/add_folder.html', {
        'form' : form,
    })


@login_required
def move_video(request):
    if request.method == 'POST':
        video_title = request.POST['video']
        folder_title = request.POST['folder']
        
        video = Video.objects.filter(title = video_title, user = request.user)
        folder = Folder.objects.get(title = folder_title, user = request.user)

        video.update(folder = folder)
        
        return redirect('main')

    else:
        videos = Video.objects.filter(user = request.user)
        folders = Folder.objects.filter(user = request.user)
        return render(request, 'folderize/move_video.html', {
            'videos' : videos,
            'folders' : folders
        })