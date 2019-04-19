# Generated by Django 2.1.1 on 2019-02-05 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='project_name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('links', models.TextField(blank=True, verbose_name='links_to_project')),
                ('image', models.ImageField(blank=True, upload_to='project_images')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_area', models.CharField(max_length=64, unique=True, verbose_name='name_area')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ProjectArea'),
        ),
    ]
