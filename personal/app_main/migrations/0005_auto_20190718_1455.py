# Generated by Django 2.2.3 on 2019-07-18 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0004_auto_20190718_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='Message',
        ),
        migrations.RemoveField(
            model_name='message',
            name='email',
        ),
        migrations.RemoveField(
            model_name='message',
            name='name',
        ),
        migrations.RemoveField(
            model_name='message',
            name='subject',
        ),
        migrations.AddField(
            model_name='message',
            name='Email',
            field=models.EmailField(blank=True, default='No E-mail', max_length=50),
        ),
        migrations.AddField(
            model_name='message',
            name='Name',
            field=models.CharField(default='No Name', max_length=40),
        ),
        migrations.AddField(
            model_name='message',
            name='Subject',
            field=models.CharField(blank=True, default='No Subject', max_length=40),
        ),
    ]
