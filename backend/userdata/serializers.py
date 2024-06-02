from rest_framework import serializers
from userdata.models import Snapshot

class SnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snapshot
        fields = ['id', 'snapshot_date', 'listening_time', 'top_genres', 'song_ids', 'artist_ids']