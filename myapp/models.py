from django.db import models


class Mentor(models.Model):
    GENDER_CHOISE = [
        ("M", "M"),
        ("F", "F"),
    ]
    LEVEL_CHOISE = [
        ("Junior", "Junior"),
        ("Middle", "Middle"),
        ("Senior", "Senior"),
    ]
    SPEC_CHOISE = [
        ("FrontEnd", "FrontEnd"),
        ("BackEnd", "BackEnd"),
        ("FullStack", "FullStack"),
    ]
    fullname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOISE, default="M")
    image = models.ImageField(upload_to='photos/mentors/')
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    level = models.CharField(max_length=7, choices=LEVEL_CHOISE, default="Junior")
    spec = models.CharField(max_length=10, choices=SPEC_CHOISE, default="FrontEnd")
    objects = models.Manager()

    def __str__(self):
        return self.fullname


class Course(models.Model):
    SPEC_CHOISE = [
        ("HTML", "HTML"),
        ("PYTHON", "PYTHON"),
        ("JS", "JS"),
        ("DJANGO", "DJANGO"),
        ("REACT", "REACT"),
    ]
    DAY_CHOISE = [
        ("Mo_We_Fr", "Mo_We_Fr"),
        ("Tu_Th_Sa", "Tu_Th_Sa"),
    ]
    TIME_CHOISE = [
        ("11:00 - 12:30", "11:00 - 12:30"),
        ("14:00 - 15:30", "14:00 - 15:30"),
        ("16:00 - 17:30", "16:00 - 17:30"),
        ("18:00 - 19:30", "18:00 - 19:30"),
    ]
    COMPLATE_CHOISE = [
        ("Provided", "Provided"),
        ("Inprocess", "Inprocess"),
        ("Notprovided", "Notprovided"),
    ]
    name = models.CharField(max_length=100)
    spec = models.CharField(max_length=7, choices=SPEC_CHOISE, default="HTML")
    duration = models.PositiveIntegerField()
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True, blank=True)
    day = models.CharField(max_length=8, choices=DAY_CHOISE, default="Mo_We_Fr")
    time = models.CharField(max_length=14, choices=TIME_CHOISE, default="11:00 - 12:30")
    complete = models.CharField(max_length=16, choices=COMPLATE_CHOISE, default="Inprocess")
    objects = models.Manager()

    def __str__(self):
        return self.name


class Lesson(models.Model):
    LESSON_CHOISE = [
        ("HTML", "HTML"),
        ("PYTHON", "PYTHON"),
        ("JS", "JS"),
        ("DJANGO", "DJANGO"),
        ("REACT", "REACT"),
    ]

    TIME_CHOISE = [
        ("11:00 - 12:30", "11:00 - 12:30"),
        ("14:00 - 15:30", "14:00 - 15:30"),
        ("16:00 - 17:30", "16:00 - 17:30"),
        ("18:00 - 19:30", "18:00 - 19:30"),
    ]

    ROOM_CHOISE = [
        ("ROOM 1", "ROOM 1"),
        ("ROOM 2", "ROOM 2"),
        ("KOWORKING", "KOWORKING"),
    ]

    COMPLATE_CHOISE = [
        ("Complate", "Complate"),
        ("NoComplate", "NoComplate"),
        ("Waiting", "Waiting"),
    ]

    lesson_name = models.CharField(max_length=100, choices=LESSON_CHOISE, default="HTML")
    lesson_data = models.DateField()
    lesson_time = models.CharField(max_length=15, choices=TIME_CHOISE, default="11:00 - 12:30")
    lesson_mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True, default="Who is Mentor")
    lesson_group = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, default="Which Course")
    lesson_room = models.CharField(max_length=100, choices=ROOM_CHOISE, default="KOWORKING")
    lesson_status = models.CharField(max_length=100, choices=COMPLATE_CHOISE, default="Complete")
    objects = models.Manager()

    def __str__(self):
        return self.lesson_name


class Student(models.Model):
    GENDER_CHOISE = [
        ("M", "M"),
        ("F", "F"),
    ]
    PAYMENT_CHOISE = [
        ("No Payed", "No Payed"),
        ("Payed", "Payed"),
    ]
    fullname = models.CharField(max_length=100, verbose_name="Имя студента")
    age = models.PositiveIntegerField(verbose_name="Возраст")
    gender = models.CharField(max_length=1, choices=GENDER_CHOISE, default="M", verbose_name="Пол студента")
    phone = models.PositiveIntegerField(verbose_name="Телефонный номер")
    email = models.EmailField(verbose_name="Почтовый адрес")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Курс")
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, verbose_name="Уроки")
    payments = models.CharField(max_length=9, choices=PAYMENT_CHOISE, default="No Payed", verbose_name="Оплата")
    objects = models.Manager()

    def __str__(self):
        return self.fullname
