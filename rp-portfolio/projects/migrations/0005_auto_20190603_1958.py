# Generated by Django 2.2.1 on 2019-06-03 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20190603_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='projects/static/projects/img'),
        ),
    ]
