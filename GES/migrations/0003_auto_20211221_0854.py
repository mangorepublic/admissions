# Generated by Django 3.1.7 on 2021-12-21 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GES', '0002_auto_20211220_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degree_programs',
            name='image',
            field=models.ImageField(default='media/uni2.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='diploma_programs',
            name='image',
            field=models.ImageField(default='media/uni2.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='hnd_programs',
            name='image',
            field=models.ImageField(default='media/uni2.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='school',
            name='image',
            field=models.ImageField(default='media/uni1.png', upload_to=''),
        ),
    ]