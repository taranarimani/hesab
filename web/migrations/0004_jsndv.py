# Generated by Django 2.2 on 2020-09-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='jsndv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=229)),
            ],
        ),
    ]
