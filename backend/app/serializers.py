
"""fields = '__all__' # поля которые переводятся в json формат(сериализуются)"""

from rest_framework import serializers
from .models import Group, Day, Lesson, Teacher

# serializors for project

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'
        

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    
    """
    Добавляю передачу данных которые хранятся в моделях: Day и Teacher, иначе 
    будут передаваться только ID(из-за связи по ключу ForeignKey)
    """
    
    teacher = serializers.StringRelatedField()
    day = serializers.StringRelatedField()
    
    class Meta:
        model = Lesson
        fields = '__all__'
        
""" 
# позволяет получить детальную информацию о преподавателе, дне
teacher = TeacherSerializer(read_only=True)
day = DaySerializer(read_only=True) # параметр read_only отвечает что данные можно только читать, но нельзя изменять через API

Я же буду передавать только название в строке, для модели с уроком этого 
хватит, тк там не нужно передавать id препода или дня, нужно чтобы
показывало название которое я прописал в функции __str__.
"""
