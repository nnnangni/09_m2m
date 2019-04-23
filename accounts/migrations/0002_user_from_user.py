# Generated by Django 2.1.5 on 2019-04-23 00:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='from_user',
            field=models.ManyToManyField(blank=True, related_name='to_user', to=settings.AUTH_USER_MODEL),
        ),
    ]