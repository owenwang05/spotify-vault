from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

import datetime

class Profile(models.Model):
    user_id = models.CharField(max_length=30)
    snapshot_cached = models.BooleanField(default=False)
    last_saved = models.DateTimeField('Last Saved', default=datetime.date.min)

    def recently_saved(self):
        return self.last_saved >= timezone.now() - datetime.timedelta(days=1)

    def total_snapshots(self):
        return self.snapshot_set.count()

    def __str__(self):
        return self.user_id

class Snapshot(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateField('Date Saved', auto_now_add=True)
    username = models.CharField(max_length=30, default='null')
    avatar_url = models.CharField(max_length=100, default='') # empty string signifies no profile picture
    listening_time = models.IntegerField(default=0) # in milliseconds
    top_genres = ArrayField(models.CharField(max_length=30), size=3, default=list)
    song_ids = ArrayField(models.CharField(max_length=30), size=5, default=list)
    artist_ids = ArrayField(models.CharField(max_length=30), size=5, default=list)

    def __str__(self):
        return self.date.isoformat()