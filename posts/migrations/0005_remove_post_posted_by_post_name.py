# Generated by Django 4.0 on 2022-01-08 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_posted_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='posted_by',
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='User', max_length=20),
        ),
    ]
