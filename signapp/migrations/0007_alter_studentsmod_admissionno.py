# Generated by Django 5.0.1 on 2024-02-24 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signapp', '0006_remove_studentsmod_id_alter_studentsmod_admissionno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsmod',
            name='admissionno',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]
