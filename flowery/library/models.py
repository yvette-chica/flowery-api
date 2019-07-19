from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    videoId = models.CharField(max_length=30)
    captions = models.TextField()
    thumbnailUrl = models.CharField(max_length=120) # TODO Save thumbnail 

    def _str_(self):
        return self.title