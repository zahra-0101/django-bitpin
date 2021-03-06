# Generated by Django 4.0.2 on 2022-02-22 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='Title')),
                ('definition', models.TextField(blank=True, null=True, verbose_name='Definition')),
            ],
        ),
        migrations.CreateModel(
            name='ScoreResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_score', models.PositiveSmallIntegerField(default=0, null=True, verbose_name='Assessed level score')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='content.content')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
