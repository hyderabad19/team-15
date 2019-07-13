# Generated by Django 2.2.2 on 2019-07-13 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('contact', models.IntegerField(default=0)),
                ('type', models.CharField(choices=[('Incharge', 'Incharge'), ('LoopManager', 'LoopManager')], default='Incharge', max_length=20)),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('verified', models.BooleanField(default=False)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.District')),
                ('mandal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Mandal')),
            ],
        ),
    ]
