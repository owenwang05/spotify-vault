from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    userID = models.CharField(max_length=32)

    def __str__(self):
        return self.userID

class UserSnapshot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    snapshotDate = models.DateField(auto_now_add=True, editable=False)
    listeningTime = models.IntegerField(default=0)
    topGenres = ArrayField(models.CharField(max_length=32), size=3, null=True)
    songIDs = ArrayField(models.CharField(max_length=32), size=5, null=True)
    artistIDs = ArrayField(models.CharField(max_length=32), size=5, null=True)

    def __str__(self):
        return self.snapshotDate

