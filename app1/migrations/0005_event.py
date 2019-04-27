# Generated by Django 2.0 on 2019-04-27 21:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0004_remove_article_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('assiged_By', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField()),
                ('organizers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
