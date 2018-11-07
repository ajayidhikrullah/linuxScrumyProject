# Generated by Django 2.0.7 on 2018-11-05 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ajayidhikrullahscrumy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goalstatus',
            name='Scrumygoals',
        ),
        migrations.AlterField(
            model_name='scrumygoals',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ajayidhikrullahscrumy', to=settings.AUTH_USER_MODEL),
        ),
    ]