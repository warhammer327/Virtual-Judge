# Generated by Django 3.0.4 on 2020-04-01 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createcontest', '0004_auto_20200331_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='createcontest',
            name='problem_note_1',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_note_2',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_note_3',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_note_4',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_note_5',
            field=models.TextField(default=' '),
        ),
    ]
