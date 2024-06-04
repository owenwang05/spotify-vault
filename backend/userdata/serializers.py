from rest_framework import serializers
from userdata.models import Snapshot

class SnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snapshot
        fields = ['snapshot_date', 'username', 'profile_picture', 'listening_time', 'top_genres', 'song_ids', 'artist_ids']