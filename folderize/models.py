from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

# Create your models here.

class Folder(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models.PROTECT
    )
    title = models.CharField(
        max_length = 250,
        null = False,
        help_text = _(
            'The title of the folder to be added.'   
        )
    )

    class Meta:
        verbose_name = 'folder'
        verbose_name_plural = 'folders'

    def __str__(self):
        return self.title


class Video(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models.PROTECT
    )
    title = models.CharField(
        max_length = 250,
        null = False,
        help_text = _(
            'The title of the video to be added.'   
        )
    )
    url = models.URLField(
        max_length = 250,
        help_text = _(
            'URL to that video.'   
        )
    )
    created_on = models.DateTimeField(
        auto_now_add = True
    )
    folder = models.ForeignKey(
        Folder,
        null = True,
        blank = True,
        on_delete = models.PROTECT,
        help_text = _(
            'The folder this video should to added to. If the list seems empty, then please add some folders first.'
        )
    )

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'

    def __str__(self):
        return self.title

