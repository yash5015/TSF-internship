# Generated by Django 3.2.7 on 2021-09-05 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
    ]