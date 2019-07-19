from django.contrib import admin

from .models import Lesson

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'videoId', 'captions', 'thumbnailUrl')

admin.site.register(Lesson, LessonAdmin)
