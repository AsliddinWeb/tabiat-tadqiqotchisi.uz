from django.db import models
import re

class Video(models.Model):
    title = models.CharField(max_length=255, verbose_name="Video sarlavhasi")
    video_number = models.PositiveIntegerField(verbose_name="Video raqami")
    description = models.TextField(verbose_name="Video haqida")
    video_url = models.URLField(verbose_name="Video linki")

    def get_drive_id(self):
        """Google Drive URL'dan file ID'ni ajratib olish"""
        match = re.search(r'/d/([a-zA-Z0-9_-]+)', self.video_url)
        if match:
            return match.group(1)
        match = re.search(r'id=([a-zA-Z0-9_-]+)', self.video_url)
        if match:
            return match.group(1)
        return ''

    def __str__(self):
        return f"{self.video_number}. {self.title}"

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videolar"
        ordering = ['video_number']


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="To'liq ismi")
    phone = models.CharField(max_length=20, verbose_name="Telefon raqami")
    message = models.TextField(verbose_name="Xabar")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqti")
    is_sent_to_telegram = models.BooleanField(default=False, verbose_name="Telegramga yuborildi")

    def __str__(self):
        return f"{self.full_name} - {self.phone}"

    class Meta:
        verbose_name = "Aloqa xabari"
        verbose_name_plural = "Aloqa xabarlari"
        ordering = ['-created_at']