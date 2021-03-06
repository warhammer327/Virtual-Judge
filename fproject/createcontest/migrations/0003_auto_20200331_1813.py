# Generated by Django 3.0.4 on 2020-03-31 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createcontest', '0002_remove_createcontest_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createcontest',
            name='problem_description',
        ),
        migrations.RemoveField(
            model_name='createcontest',
            name='problem_input',
        ),
        migrations.RemoveField(
            model_name='createcontest',
            name='problem_name',
        ),
        migrations.RemoveField(
            model_name='createcontest',
            name='problem_output',
        ),
        migrations.AddField(
            model_name='createcontest',
            name='contest_name',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_description_1',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_description_2',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_description_3',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_description_4',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_description_5',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_input_1',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_input_2',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_input_3',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_input_4',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_input_5',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_name_1',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_name_2',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_name_3',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_name_4',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_name_5',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_output_1',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_output_2',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_output_3',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_output_4',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_output_5',
            field=models.TextField(default='-'),
        ),
    ]
