# Generated by Django 5.0.1 on 2024-03-03 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signapp', '0009_tablefordoubt_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsmod',
            name='password',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
    ]
