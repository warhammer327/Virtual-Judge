# Generated by Django 3.0.6 on 2020-06-12 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createcontest', '0014_auto_20200612_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='createcontest',
            name='problem_pic_2',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_pic_3',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_pic_4',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_pic_5',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_pic_url_2',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_pic_url_3',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_pic_url_4',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='createcontest',
            name='problem_pic_url_5',
            field=models.TextField(default='-'),
        ),
    ]
