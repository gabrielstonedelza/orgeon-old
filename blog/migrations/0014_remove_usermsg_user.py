# Generated by Django 3.0.3 on 2020-02-26 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200226_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermsg',
            name='user',
        ),
    ]
