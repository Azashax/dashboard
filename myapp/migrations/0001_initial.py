# Generated by Django 3.2.5 on 2021-07-13 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('spec', models.CharField(choices=[('HTML', 'HTML'), ('PYTHON', 'PYTHON'), ('JS', 'JS'), ('DJANGO', 'DJANGO'), ('REACT', 'REACT')], default='HTML', max_length=7)),
                ('duration', models.PositiveIntegerField()),
                ('day', models.CharField(choices=[('Mo_We_Fr', 'Mo_We_Fr'), ('Tu_Th_Sa', 'Tu_Th_Sa')], default='Mo_We_Fr', max_length=8)),
                ('time', models.CharField(choices=[('11:00 - 12:30', '11:00 - 12:30'), ('14:00 - 15:30', '14:00 - 15:30'), ('16:00 - 17:30', '16:00 - 17:30'), ('18:00 - 19:30', '18:00 - 19:30')], default='11:00 - 12:30', max_length=14)),
                ('complete', models.CharField(choices=[('Provided', 'Provided'), ('Inprocess', 'Inprocess'), ('Notprovided', 'Notprovided')], default='Inprocess', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(choices=[('HTML', 'HTML'), ('PYTHON', 'PYTHON'), ('JS', 'JS'), ('DJANGO', 'DJANGO'), ('REACT', 'REACT')], default='HTML', max_length=100)),
                ('lesson_data', models.DateField()),
                ('lesson_time', models.CharField(choices=[('11:00 - 12:30', '11:00 - 12:30'), ('14:00 - 15:30', '14:00 - 15:30'), ('16:00 - 17:30', '16:00 - 17:30'), ('18:00 - 19:30', '18:00 - 19:30')], default='11:00 - 12:30', max_length=15)),
                ('lesson_room', models.CharField(choices=[('ROOM 1', 'ROOM 1'), ('ROOM 2', 'ROOM 2'), ('KOWORKING', 'KOWORKING')], default='KOWORKING', max_length=100)),
                ('lesson_status', models.CharField(choices=[('Complate', 'Complate'), ('NoComplate', 'NoComplate'), ('Waiting', 'Waiting')], default='Complete', max_length=100)),
                ('lesson_group', models.ForeignKey(default='Which Course', null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.course')),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=1)),
                ('image', models.ImageField(upload_to='photos/mentors/')),
                ('phone', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('level', models.CharField(choices=[('Junior', 'Junior'), ('Middle', 'Middle'), ('Senior', 'Senior')], default='Junior', max_length=7)),
                ('spec', models.CharField(choices=[('FrontEnd', 'FrontEnd'), ('BackEnd', 'BackEnd'), ('FullStack', 'FullStack')], default='FrontEnd', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100, verbose_name='Имя студента')),
                ('age', models.PositiveIntegerField(verbose_name='Возраст')),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=1, verbose_name='Пол студента')),
                ('phone', models.PositiveIntegerField(verbose_name='Телефонный номер')),
                ('email', models.EmailField(max_length=254, verbose_name='Почтовый адрес')),
                ('payments', models.CharField(choices=[('No Payed', 'No Payed'), ('Payed', 'Payed')], default='No Payed', max_length=9, verbose_name='Оплата')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.course', verbose_name='Курс')),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.lesson', verbose_name='Уроки')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson_mentor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.mentor'),
        ),
        migrations.AddField(
            model_name='course',
            name='mentor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.mentor'),
        ),
    ]
