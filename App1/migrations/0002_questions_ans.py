# Generated by Django 3.0 on 2021-09-17 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='ans',
            field=models.CharField(default='a', max_length=1),
            preserve_default=False,
        ),
    ]
