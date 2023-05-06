# Generated by Django 4.2.1 on 2023-05-06 00:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('completed', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('userOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.user')),
            ],
        ),
    ]
