# Generated by Django 2.2.3 on 2019-07-22 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0008_auto_20190723_0015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Message',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='Image',
        ),
    ]
