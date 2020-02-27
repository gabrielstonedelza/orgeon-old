# Generated by Django 3.0.3 on 2020-02-26 22:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_auto_20200226_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='need_replies',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Usermsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unread_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.InstantMessage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
