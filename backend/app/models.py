from django.db import models
from datetime import time, timedelta, datetime

# Create your models here.

class Group(models.Model):
    group_name = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return f"Група {self.group_name}"


class Day(models.Model):
    DaysOfWeek = [    
    ('Понедельник', 'Понедельник'),
    ('Вторник', 'Вторник'),
    ('Среда', 'Среда'),
    ('Четверг', 'Четверг'),
    ('Пятница', 'Пятница'),
    ('Суббота', 'Суббота')
    ]
    group_name = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group_key')
    day = models.CharField(max_length=20, choices=DaysOfWeek, unique=True)
    
    def __str__(self):
        return f"{self.day}"

    
class Teacher(models.Model):
    name = models.CharField(max_length=50, default="-")
    
    def __str__(self):
        return f"{self.name}"

    
class Lesson(models.Model):
    subjects = [
        ('Математика', 'Математика'),
        ('Физика', 'Физика'),
        ('Русский язык', 'Русский язык'),
        ('Белорусский язык', 'Белорусский язык'),
        ('Русская литература', 'Русская литература'),
        ('Бел Литература', 'Беларусская литература'),
        ('Английский язык', 'Английский язык'),
        ('Биология', 'Биология'),
        ('Химия', 'Химия'),
        ('География', 'География'),
        ('Сольфеджио', 'Сольфеджио'),
        ('ПДД', 'ПДД'),
        ('Эл. Теория Музыки', 'Эл. Теория музыки'),
        ('Хоровой класс', 'Хоровой класс'),
        ('Хороведение', 'Хороведение'),
        ('Физ-ра', 'Физ-ра'),
        ('Информатика', 'Информатика'),
        ('МКТ', 'МКТ'),
        ('История', 'История'),
        ('Обществоведение', 'Обществоведение'),
        ('Классный час', 'Классный час'),
        ('---', 'Ничего'),
        ('Другое', 'Другое')
    ]
    
    time_starts_choices = [
        (time(8, 30), '8:30'),
        (time(9, 25), '9:25'),
        (time(10, 20), '10:20'),
        (time(11, 15), '11:15'),
        (time(12, 20), '12:20'),
        (time(13, 15), '13:15'),
        (time(14, 10), '14:10'),
        (time(15, 5), '15:05'),
        (time(16, 0), '16:00'),
        (time(16, 55), '16:55'),
        (time(17, 50), '17:50'),
        (time(18, 45), '18:45')
    ]

    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='day_key')
    subject =  models.CharField(max_length=20, choices=subjects)
    lesson_starts_time = models.TimeField(choices=time_starts_choices)
    lesson_ends_time = models.TimeField(editable=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_key')
    classroom = models.CharField(max_length=10)
    
    """обязательное название для метода переопределения стандартного сохранения модели в Django -- save"""
    def save(self, *args, **kwargs):
        """Автоматическое сохрание lesson_ends_time как lesson_starts_time + 45 минут"""
        if self.time_starts_choices: # проверка на присутствие lesson_starts_time(установлено ли оно)
            self.lesson_ends_time = (datetime.combine(datetime.today(), self.lesson_starts_time) + timedelta(minutes=45)).time()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.subject} {self.lesson_starts_time.strftime('%H:%M')}-{self.lesson_ends_time.strftime('%H:%M')} {self.classroom}"