# Generated by Django 3.0.3 on 2020-07-27 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200727_1826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='coverpic',
            new_name='photo',
        ),
    ]
