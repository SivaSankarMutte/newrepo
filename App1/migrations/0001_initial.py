# Generated by Django 3.0 on 2021-09-17 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(max_length=500)),
                ('opt1', models.CharField(max_length=100)),
                ('opt2', models.CharField(max_length=100)),
                ('opt3', models.CharField(max_length=100)),
                ('opt4', models.CharField(max_length=100)),
            ],
        ),
    ]
