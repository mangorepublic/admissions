# Generated by Django 3.1.7 on 2021-12-21 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GES', '0003_auto_20211221_0854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='degree_programs',
            old_name='degree_schools',
            new_name='school',
        ),
        migrations.RenameField(
            model_name='diploma_programs',
            old_name='diploma_schools',
            new_name='school',
        ),
        migrations.RenameField(
            model_name='hnd_programs',
            old_name='hnd_schools',
            new_name='school',
        ),
        migrations.RemoveField(
            model_name='school',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='school',
            name='diploma',
        ),
        migrations.RemoveField(
            model_name='school',
            name='hnd',
        ),
    ]
