# Generated by Django 2.2.1 on 2019-06-03 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20190603_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='projects/img'),
        ),
    ]
