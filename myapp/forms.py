from django import forms
from .models import *

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['fullname', 'age', 'gender', 'phone', 'email', 'course', 'lesson', 'payments']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'lesson': forms.Select(attrs={'class': 'form-control'}),
            'payments': forms.Select(attrs={'class': 'form-control'}),
        }


class CoursesForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'spec', 'duration', 'mentor', 'day', 'time', 'complete']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'spec': forms.Select(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'mentor': forms.Select(attrs={'class': 'form-control'}),
            'day': forms.Select(attrs={'class': 'form-control'}),
            'time': forms.Select(attrs={'class': 'form-control'}),
            'complete': forms.Select(attrs={'class': 'form-control'}),
        }


class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ['fullname', 'age', 'gender', 'image', 'phone', 'email', 'level', 'spec']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file', 'type': 'file'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            'spec': forms.Select(attrs={'class': 'form-control'}),
        }


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['lesson_name', 'lesson_data', 'lesson_time', 'lesson_mentor', 'lesson_group', 'lesson_room', 'lesson_status']
        widgets = {
            'lesson_name': forms.Select(attrs={'class': 'form-control'}),
            'lesson_data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'lesson_time': forms.Select(attrs={'class': 'form-control'}),
            'lesson_mentor': forms.Select(attrs={'class': 'form-control'}),
            'lesson_group': forms.Select(attrs={'class': 'form-control'}),
            'lesson_room': forms.Select(attrs={'class': 'form-control'}),
            'lesson_status': forms.Select(attrs={'class': 'form-control'}),
        }











