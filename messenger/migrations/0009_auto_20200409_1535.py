# Generated by Django 3.0.4 on 2020-04-09 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0008_message_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='forward_email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='organization',
            name='forward_phone',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='organization',
            name='response_msg',
            field=models.CharField(default='Thank you, your message has been received', max_length=255),
        ),
    ]
