# Generated by Django 2.0 on 2019-04-27 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
