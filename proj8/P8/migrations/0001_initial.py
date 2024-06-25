# Generated by Django 5.0.6 on 2024-06-20 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=40)),
                ('course_name', models.CharField(max_length=100)),
                ('course_credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_code', models.CharField(max_length=100)),
                ('meeting_dt', models.DateField(auto_now_add=True)),
                ('meeting_subject', models.CharField(max_length=100)),
                ('meeting_up', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_usn', models.CharField(max_length=20)),
                ('student_name', models.CharField(max_length=100)),
                ('student_sem', models.IntegerField()),
                ('enrolment', models.ManyToManyField(to='P8.course')),
            ],
        ),
    ]
