# Generated by Django 3.2.8 on 2021-11-05 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviestore', '0008_alter_movie_user_charge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='user_charge',
            new_name='usr_charge',
        ),
    ]
