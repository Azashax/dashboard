# Generated by Django 3.2.5 on 2021-07-13 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_mentor',
            field=models.ForeignKey(default='Who is Mentor', null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.mentor'),
        ),
    ]
