# Generated by Django 5.1.2 on 2024-10-29 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.IntegerField(blank=None, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=70)),
                ('designation', models.CharField(max_length=70)),
                ('feedback', models.TextField(max_length=255)),
            ],
        ),
    ]
