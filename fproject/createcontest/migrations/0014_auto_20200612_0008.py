# Generated by Django 3.0.6 on 2020-06-12 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('createcontest', '0013_createcontest_problem_pic_name_1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createcontest',
            old_name='problem_pic_name_1',
            new_name='problem_pic_1',
        ),
        migrations.RenameField(
            model_name='createcontest',
            old_name='problem_picurl_1',
            new_name='problem_pic_url_1',
        ),
    ]
