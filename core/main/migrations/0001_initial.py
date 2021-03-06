# Generated by Django 4.0.5 on 2022-06-11 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=30, verbose_name='Homepage name1')),
                ('name2', models.CharField(max_length=30, verbose_name='Homepage name2')),
                ('about', models.TextField(verbose_name='Homepage about')),
                ('img', models.ImageField(upload_to='media', verbose_name='Homepage img')),
            ],
            options={
                'verbose_name': 'Homepage',
                'verbose_name_plural': 'Homepages',
            },
        ),
    ]
