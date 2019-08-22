from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LessonSerializer
from .models import Lesson

class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
