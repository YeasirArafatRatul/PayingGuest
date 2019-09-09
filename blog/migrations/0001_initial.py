# Generated by Django 2.0.7 on 2019-04-19 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=101)),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=1000)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_image', models.ImageField(upload_to='post_images')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]