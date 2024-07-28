# Generated by Django 4.2.7 on 2023-12-04 09:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0002_sasquatch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sasquatch',
            name='number',
        ),
        migrations.AddField(
            model_name='sasquatch',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sasquatch',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]