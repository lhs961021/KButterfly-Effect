# Generated by Django 3.2.7 on 2021-10-03 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('date_start', models.DateTimeField()),
                ('date_deadline', models.DateTimeField()),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('p_or_o', models.BooleanField(default=False)),
                ('after', models.BooleanField(default=False)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('personal_eco_point', models.IntegerField(default=0)),
                ('name', models.CharField(default='', max_length=64)),
                ('phnum', models.CharField(default='', max_length=12)),
                ('image', models.ImageField(null=True, upload_to='user/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
