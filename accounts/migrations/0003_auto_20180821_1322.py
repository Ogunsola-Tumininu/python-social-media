# Generated by Django 2.1 on 2018-08-21 12:22

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_image'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('lagos', django.db.models.manager.Manager()),
            ],
        ),
    ]
