# Generated by Django 2.2.2 on 2019-07-13 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_school_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='address',
            field=models.CharField(default='new', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='sai', max_length=20),
        ),
    ]
