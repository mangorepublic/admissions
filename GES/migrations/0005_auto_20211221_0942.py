# Generated by Django 3.1.7 on 2021-12-21 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GES', '0004_auto_20211221_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='degree_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='degree_programs',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GES.degree_type'),
        ),
        migrations.AddField(
            model_name='diploma_programs',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GES.degree_type'),
        ),
        migrations.AddField(
            model_name='hnd_programs',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GES.degree_type'),
        ),
    ]
