# Generated by Django 4.2.5 on 2023-12-11 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0008_attendance_comments_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='comments',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='leave',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
