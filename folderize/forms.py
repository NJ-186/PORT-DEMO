from django.forms import ModelForm
from .models import Video, Folder


class VideoForm(ModelForm):

    class Meta:
        model = Video
        fields = ['title','url','folder']

    # custom __init__ - to fetch only the videos, that particular user has added
    
    def __init__(self, request, *args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)
        
        if request.method == 'GET':
            self.fields['folder'].queryset = Folder.objects.filter(user = request.user)

class FolderForm(ModelForm):

    class Meta:
        model = Folder
        fields = ['title']