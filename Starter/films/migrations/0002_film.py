# Generated by Django 3.2.8 on 2024-12-09 05:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('users', models.ManyToManyField(related_name='films', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
