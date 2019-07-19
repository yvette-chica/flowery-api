from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LessonSerializer
from .models import Lesson

class LessonView(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
