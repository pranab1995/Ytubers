# Generated by Django 3.1.7 on 2021-03-11 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_team_insta_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='youtube_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
