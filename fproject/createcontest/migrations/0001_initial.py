# Generated by Django 3.0.4 on 2020-03-31 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Createcontest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('problem_name', models.CharField(max_length=50)),
                ('problem_description', models.TextField()),
                ('problem_input', models.TextField()),
                ('problem_output', models.TextField()),
            ],
        ),
    ]
