# Generated by Django 2.1.5 on 2019-02-05 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=100)),
                ('bodytext', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
