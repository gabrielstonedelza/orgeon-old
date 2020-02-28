# Generated by Django 3.0.3 on 2020-02-28 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0016_auto_20200228_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckLoginLogout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_code', models.IntegerField()),
                ('date_and_time_logged', models.DateTimeField(default=django.utils.timezone.now)),
                ('logged_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
