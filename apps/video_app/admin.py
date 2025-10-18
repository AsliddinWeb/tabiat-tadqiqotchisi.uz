from django.contrib import admin
from .models import Video, ContactMessage

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_number', 'title', 'video_url')
    list_filter = ('video_number',)
    search_fields = ('title', 'description')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'created_at', 'is_sent_to_telegram')
    list_filter = ('is_sent_to_telegram', 'created_at')
    search_fields = ('full_name', 'phone', 'message')
    readonly_fields = ('created_at',)