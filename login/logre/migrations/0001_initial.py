# Generated by Django 4.0.5 on 2022-07-08 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, verbose_name=50)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
