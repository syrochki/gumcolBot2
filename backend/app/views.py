"""
Набор представлений, который автоматически создаёт CRUD API для модели
"""

from django.shortcuts import render
from rest_framework import viewsets
from .models import Group, Day, Lesson, Teacher
from .serializers import GroupSerializer, DaySerializer, LessonSerializer, TeacherSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    
class DayViewSet(viewsets.ModelViewSet):
    serializer_class = DaySerializer
    queryset = Day.objects.all()
    
class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    
class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

# загрузка стандартной страницы
def home_page(request):
    return render(request, 'home_page.html')