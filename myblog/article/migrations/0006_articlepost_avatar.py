# Generated by Django 2.2.5 on 2019-10-08 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_articlepost_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='article/%Y%m%d/'),
        ),
    ]
