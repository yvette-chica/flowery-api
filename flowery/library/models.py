from django.db import models
from youtube_transcript_api import YouTubeTranscriptApi

class Lesson(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    videoId = models.CharField(max_length=30)
    captions = models.TextField(null=True, blank=True)
    thumbnailUrl = models.CharField(max_length=120) # TODO Save thumbnail 

    def _str_(self):
        return self.title
    
    def fetch_captions(self):
        return YouTubeTranscriptApi.get_transcript(self.videoId) 
        
    def save(self, *args, **kwargs):
        if not self.captions:
            self.captions = self.fetch_captions()
        super().save(*args, **kwargs)