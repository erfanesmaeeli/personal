# Generated by Django 2.2.3 on 2019-07-25 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0011_auto_20190725_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
