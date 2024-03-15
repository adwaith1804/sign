# Generated by Django 5.0.1 on 2024-03-12 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signapp', '0019_alter_attendancemod_attendancestatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamModel',
            fields=[
                ('exam_key', models.AutoField(primary_key=True, serialize=False)),
                ('class_student', models.CharField(max_length=5)),
                ('question', models.CharField(max_length=100)),
                ('option1', models.CharField(max_length=50)),
                ('option2', models.CharField(max_length=50)),
                ('option3', models.CharField(max_length=50)),
                ('teacher_id', models.CharField(max_length=5)),
                ('current_date', models.DateField(auto_now=True)),
                ('exam_date', models.DateField(null=True)),
            ],
        ),
    ]