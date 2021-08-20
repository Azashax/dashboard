from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request):
    coursesItem = Course.objects.all()
    mentorsItem = Mentor.objects.all()
    lessonsItem = Lesson.objects.all()
    studentsItem = Student.objects.all()

    if request.method == "POST" and request.POST.get("course_id"):
        studentsItem = Student.objects.filter(course=request.POST.get("course_id"))
    else:
        studentsItem = Student.objects.all()

    if request.method == "POST" and request.POST.get("course_id"):
        lessonsItem = Lesson.objects.filter(lesson_group=request.POST.get("course_id"))
    else:
        lessonsItem = Lesson.objects.all()

    paginator = Paginator(coursesItem, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "studentsItem": studentsItem,
        "coursesItem": coursesItem,
        "mentorsItem": mentorsItem,
        "lessonsItem": lessonsItem,
        "page_obj": page_obj,
    }

    return render(request, 'myapp/index.html', context)


def students(request):
    form = StudentsForm
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")

    context = {
        "form": form,
    }
    return render(request, 'myapp/students.html', context)


def courses(request):
    form = CoursesForm
    if request.method == "POST":
        form = CoursesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")

    context = {
        "form": form,
    }
    return render(request, 'myapp/courses.html', context)


def mentors(request):
    form = MentorForm
    if request.method == "POST":
        form = MentorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("homepage")
        else:
            messages.info(request, 'error')

    context = {
        "form": form,
    }

    return render(request, 'myapp/mentor.html', context)


def lessons(request):
    form = LessonForm
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
        else:
            messages.info(request, "error")

    context = {
        "form": form,
    }

    return render(request, 'myapp/lesson.html', context)


def action_page(request, pk):
    order = Course.objects.get(id=pk)
    form = CoursesForm(instance=order)

    if request.method == "POST":
        form = CoursesForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form,
    }
    return render(request, 'myapp/actions.html', context)


def delete_page(request, pk):
    order = Course.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect("/")

    context = {
        "item": order,
    }

    return render(request, 'myapp/delete.html', context)
