# Generated by Django 4.0.5 on 2022-06-18 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_homepagecategory1_homepagecategory2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Category name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Shoose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Shoose name')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catshoose', to='main.category')),
            ],
            options={
                'verbose_name': 'Shoose',
                'verbose_name_plural': 'Shooses',
            },
        ),
    ]
