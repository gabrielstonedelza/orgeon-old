# Generated by Django 3.0.3 on 2020-04-18 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='chat_id',
            field=models.IntegerField(default=1),
        ),
    ]