# Generated by Django 2.2.5 on 2019-10-07 10:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_articlepost_total_views'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commen',
            new_name='Comment',
        ),
    ]