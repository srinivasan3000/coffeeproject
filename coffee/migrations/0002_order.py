# Generated by Django 3.1 on 2020-09-10 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('food', models.CharField(max_length=250)),
                ('number', models.IntegerField()),
            ],
        ),
    ]
