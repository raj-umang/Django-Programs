# Generated by Django 5.0.6 on 2024-07-25 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A12', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=100)),
                ('field2', models.IntegerField()),
            ],
        ),
    ]
