# Generated by Django 3.0 on 2021-09-21 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0004_auto_20210921_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, 'Guest'), (2, 'Professor'), (3, 'User')], default=1),
        ),
        migrations.AddField(
            model_name='user',
            name='uimg',
            field=models.ImageField(default='dummyProfile.png', upload_to='Profilepics/'),
        ),
        migrations.CreateModel(
            name='Rolereq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rltype', models.IntegerField(choices=[(2, 'Professor'), (3, 'Student')])),
                ('pfe', models.ImageField(default='dummyProfile.png', upload_to='Rolereqpics/')),
                ('is_checked', models.BooleanField(default=False)),
                ('uname', models.CharField(max_length=50)),
                ('ud', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
