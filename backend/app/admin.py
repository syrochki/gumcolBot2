from django.contrib import admin
from .models import Group, Day, Teacher, Lesson

# Register your models here.

# в модели группы будет показываться модель дней для заполнения(7 -- пропуски)
class DayInLine(admin.TabularInline):
    model = Day
    extra = 7

# показываются уроки в модели дня
class LessonInLine(admin.TabularInline):
    model = Lesson
    extra = 1

'''регистрация моделей в админ панели'''

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', )
    search_fields = ('group_name', )
    inlines = [DayInLine]

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('day', 'group_name')
    list_filter = ('day', 'group_name')
    inlines = [LessonInLine]
    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    list_filter = ('name', )

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('subject', 'classroom', 'teacher')
    search_fields = ('subject', 'classroom', 'teacher__name')
    list_filter = ('subject', 'classroom', 'teacher__name', 'lesson_starts_time')
