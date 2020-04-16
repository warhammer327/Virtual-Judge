from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Createcontest(models.Model):

	contest_name = models.CharField(max_length=50,default='-')
	contest_setter = models.CharField(max_length=50,default='-')

	problem_name_1 = models.CharField(max_length=50,default='-')
	problem_time_limit_1 = models.CharField(max_length=50,default='-')
	problem_memory_limit_1 = models.CharField(max_length=50,default='-')
	problem_description_1 = RichTextField(default='-');
	problem_input_1 = RichTextField(default='-');
	problem_output_1 = RichTextField(default='-');
	problem_note_1 = RichTextField(default=' ')

	problem_name_2 = models.CharField(max_length=50,default='-')
	problem_time_limit_2 = models.CharField(max_length=50,default='-')
	problem_memory_limit_2 = models.CharField(max_length=50,default='-')
	problem_description_2 = RichTextField(default='-');
	problem_input_2 = RichTextField(default='-');
	problem_output_2 = RichTextField(default='-');
	problem_note_2 = RichTextField(default=' ')

	problem_name_3 = models.CharField(max_length=50,default='-')
	problem_time_limit_3 = models.CharField(max_length=50,default='-')
	problem_memory_limit_3 = models.CharField(max_length=50,default='-')
	problem_description_3 = RichTextField(default='-');
	problem_input_3 = RichTextField(default='-');
	problem_output_3 = RichTextField(default='-');
	problem_note_3 = RichTextField(default=' ')

	problem_name_4 = models.CharField(max_length=50,default='-')
	problem_time_limit_4 = models.CharField(max_length=50,default='-')
	problem_memory_limit_4 = models.CharField(max_length=50,default='-')
	problem_description_4 = RichTextField(default='-');
	problem_input_4 = RichTextField(default='-');
	problem_output_4 = RichTextField(default='-');
	problem_note_4 = RichTextField(default=' ')

	problem_name_5 = models.CharField(max_length=50,default='-')
	problem_time_limit_5 = models.CharField(max_length=50,default='-')
	problem_memory_limit_5 = models.CharField(max_length=50,default='-')
	problem_description_5 = RichTextField(default='-');
	problem_input_5 = RichTextField(default='-');
	problem_output_5 = RichTextField(default='-');
	problem_note_5 = RichTextField(default=' ')

	def __str__(self):
		return self.contest_name
