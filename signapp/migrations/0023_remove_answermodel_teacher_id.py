# Generated by Django 5.0.1 on 2024-03-15 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signapp', '0022_answermodel_teacher_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answermodel',
            name='teacher_id',
        ),
    ]
