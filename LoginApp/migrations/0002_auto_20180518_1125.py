# Generated by Django 2.0.5 on 2018-05-18 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]