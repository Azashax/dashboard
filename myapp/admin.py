from django.contrib import admin

from .models import Mentor, Course, Student, Lesson

class MentorAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'age', 'gender', 'image', 'phone', 'email', 'level', 'spec']
    list_display_links = ['id', 'fullname']
    search_fields = ['fullname', 'gender', 'level', 'spec']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'spec', 'duration', 'mentor', 'day', 'time']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'spec', 'duration', 'mentor', 'day', 'time']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'age', 'gender', 'phone', 'email', 'course', 'lesson', 'payments']
    list_display_links = ['id', 'fullname']
    search_fields = ['fullname', 'gender', 'phone', 'email', 'course']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'lesson_name', 'lesson_data', 'lesson_time', 'lesson_mentor', 'lesson_group', 'lesson_room']
    list_display_links = ['id', 'lesson_name']
    search_fields = ['lesson_name', 'lesson_data', 'lesson_time', 'lesson_mentor', 'lesson_group', 'lesson_room']

admin.site.register(Mentor, MentorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Lesson, LessonAdmin)
