# Generated by Django 5.2 on 2025-05-07 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0002_profile_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
