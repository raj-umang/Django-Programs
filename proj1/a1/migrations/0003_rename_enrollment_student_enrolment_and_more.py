# Generated by Django 5.0.6 on 2024-06-13 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0002_course_course_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='enrollment',
            new_name='enrolment',
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=100),
        ),
    ]
