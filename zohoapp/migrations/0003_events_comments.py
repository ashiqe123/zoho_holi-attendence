# Generated by Django 4.2.5 on 2023-12-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0002_events_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='comments',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
