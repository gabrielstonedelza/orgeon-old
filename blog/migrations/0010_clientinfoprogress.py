# Generated by Django 3.0.3 on 2020-05-10 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_auto_20200420_2024'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientInfoProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(blank=True, help_text="Leave blank if client doesn't have any.", max_length=255, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('emergency_phone', models.CharField(blank=True, help_text="Leave blank if client doesn't have any.", max_length=20)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='Male', max_length=10)),
                ('client_image', models.ImageField(blank=True, default='client.jpg', upload_to='client_images')),
                ('next_of_kin', models.CharField(blank=True, help_text="Leave blank if client doesn't have any.", max_length=50)),
                ('issue', models.TextField()),
                ('progress', models.CharField(choices=[('Assessment', 'Assessment'), ('Development', 'Development'), ('Planning', 'Planning'), ('Implementation', 'Implementation'), ('Evaluation', 'Evaluation'), ('Star', 'Star')], default='Assessment', help_text='Choose current level for your client.', max_length=30)),
                ('date_issued', models.DateTimeField(auto_now_add=True)),
                ('accessment_officer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
