# Generated by Django 2.2.3 on 2019-07-25 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0009_auto_20190723_0031'),
    ]

    operations = [
        migrations.CreateModel(
            name='PythonCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='Python', max_length=40)),
                ('Title', models.CharField(max_length=80, null=True)),
                ('Description', models.TextField(blank=True)),
                ('Image', models.FileField(blank=True, null=True, upload_to='')),
                ('DateCreate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='Description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='Name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Title',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
