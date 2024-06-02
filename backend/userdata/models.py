from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

import datetime

class Profile(models.Model):
    user_id = models.CharField(max_length=32)
    last_modified = models.DateTimeField('Last Modified', auto_now=True)
    snapshot_cached = models.BooleanField(default=False)

    def recently_modified(self):
        return self.last_modified <= timezone.now() - datetime.timedelta(days=1)

    def total_snapshots(self):
        return self.snapshot_set.count()

    def __str__(self):
        return self.user_id

class Snapshot(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    snapshot_date = models.DateField('Snapshot Date', auto_now_add=True)
    listening_time = models.IntegerField(default=0)
    top_genres = ArrayField(models.CharField(max_length=32), size=3, null=True)
    song_ids = ArrayField(models.CharField(max_length=32), size=5, null=True)
    artist_ids = ArrayField(models.CharField(max_length=32), size=5, null=True)

    def __str__(self):
        return self.snapshot_date.isoformat()

