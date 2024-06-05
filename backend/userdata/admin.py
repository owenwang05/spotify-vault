from django.contrib import admin

from .models import Profile, Snapshot

class SnapshotInline(admin.TabularInline):
    model = Snapshot
    extra = 0

class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user_id', 'snapshot_cached']}),
    ]
    inlines = [SnapshotInline]
    list_display = ['user_id', 'last_saved', 'total_snapshots']

admin.site.register(Profile, ProfileAdmin)