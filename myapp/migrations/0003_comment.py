# Generated by Django 3.2.9 on 2021-12-06 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_descriptions_room_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=500)),
            ],
        ),
    ]