# Generated by Django 3.2.8 on 2021-11-04 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviestore', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]