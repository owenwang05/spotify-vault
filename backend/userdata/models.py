from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

import datetime

TOP_GENRES_LENGTH = 5
TOP_LIST_LENGTH = 5

class Profile(models.Model):
    user_id = models.CharField(max_length=30)
    snapshot_cached = models.BooleanField(default=False)
    last_saved = models.DateTimeField('Last Saved', default=datetime.date.min)

    def recently_saved(self):
        return False
        return self.last_saved >= timezone.now() - datetime.timedelta(days=1)

    def total_snapshots(self):
        return self.snapshot_set.count()

    def __str__(self):
        return self.user_id

class Snapshot(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField('Date Saved', auto_now_add=True)
    username = models.CharField(max_length=30, default='null')
    avatar_url = models.CharField(max_length=100, default='') # empty string signifies no profile picture
    listening_time = models.IntegerField(default=0) # in milliseconds
    top_genres = ArrayField(models.CharField(max_length=30), size=TOP_GENRES_LENGTH, default=list)
    top_songs = models.JSONField(default=dict)
    top_artists = models.JSONField(default=dict)

    def __str__(self):
        return self.date.isoformat()