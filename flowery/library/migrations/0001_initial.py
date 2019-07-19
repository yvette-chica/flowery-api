# Generated by Django 2.2.3 on 2019-07-19 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('videoId', models.CharField(max_length=30)),
                ('captions', models.TextField()),
                ('thumbnailUrl', models.CharField(max_length=120)),
            ],
        ),
    ]