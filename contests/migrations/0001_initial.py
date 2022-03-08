# Generated by Django 4.0.1 on 2022-03-08 09:54

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(max_length=255, verbose_name='contest title')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='contest description')),
                ('start_date', models.DateField(verbose_name='contest start date')),
                ('end_date', models.DateField(verbose_name='contest end date')),
                ('published', models.BooleanField(default=False, verbose_name='published')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContestRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('rate', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, "Value can't be less than 1"), django.core.validators.MaxValueValidator(10, "Value can't be bigger than 10")], verbose_name='participant rate')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(max_length=255, verbose_name='story title')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
