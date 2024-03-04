# Generated by Django 4.2.5 on 2023-11-13 22:18

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
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.CharField(max_length=255)),
                ('frequency', models.CharField(blank=True, choices=[('DAILY', 'Daily'), ('WEEKLY', 'Weekly'), ('MONTHLY', 'Monthly'), ('YEARLY', 'Yearly')], max_length=10, null=True)),
                ('until', models.DateTimeField(blank=True, null=True)),
                ('byday', models.CharField(blank=True, max_length=50, null=True)),
                ('requestDescription', models.TextField(blank=True, null=True)),
                ('requestGranted', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]