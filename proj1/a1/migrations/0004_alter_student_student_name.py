# Generated by Django 5.0.6 on 2024-06-13 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0003_rename_enrollment_student_enrolment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_name',
            field=models.CharField(max_length=100),
        ),
    ]
