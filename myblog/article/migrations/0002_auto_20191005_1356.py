# Generated by Django 2.2.5 on 2019-10-05 05:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
