# Generated by Django 2.2.3 on 2019-07-18 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0003_auto_20190630_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(default='no name', max_length=40),
        ),
    ]
