from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
import datetime
# Create your models here.
class Createcontest(models.Model):

	contest_name = models.CharField(max_length=50,null=True)
	contest_setter = models.CharField(max_length=50,null=True)
	contest_time = models.DateTimeField(null=True,default=datetime.date.today)

	problem_name_1 = models.CharField(max_length=50,null=True)
	problem_time_limit_1 = models.CharField(max_length=50,null=True)
	problem_memory_limit_1 = models.CharField(max_length=50,null=True)
	problem_description_1 = RichTextField(null=True);
	problem_input_1 = RichTextField(null=True)
	problem_output_1 = RichTextField(null=True)
	problem_note_1 = RichTextField(null=True)
	problem_pic_url_1 = models.TextField(default="-")
	problem_pic_1 = models.TextField(null=True)

	problem_name_2 = models.CharField(max_length=50,null=True)
	problem_time_limit_2 = models.CharField(max_length=50,null=True)
	problem_memory_limit_2 = models.CharField(max_length=50,null=True)
	problem_description_2 = RichTextField(null=True);
	problem_input_2 = RichTextField(null=True);
	problem_output_2 = RichTextField(null=True);
	problem_note_2 = RichTextField(null=True)
	problem_pic_url_2 = models.TextField(default="-")
	problem_pic_2 = models.TextField(null=True)

	problem_name_3 = models.CharField(max_length=50,null=True)
	problem_time_limit_3 = models.CharField(max_length=50,null=True)
	problem_memory_limit_3 = models.CharField(max_length=50,null=True)
	problem_description_3 = RichTextField(null=True);
	problem_input_3 = RichTextField(null=True);
	problem_output_3 = RichTextField(null=True);
	problem_note_3 = RichTextField(null=True)
	problem_pic_url_3 = models.TextField(default="-")
	problem_pic_3 = models.TextField(null=True)

	problem_name_4 = models.CharField(max_length=50,null=True)
	problem_time_limit_4 = models.CharField(max_length=50,null=True)
	problem_memory_limit_4 = models.CharField(max_length=50,null=True)
	problem_description_4 = RichTextField(null=True);
	problem_input_4 = RichTextField(null=True);
	problem_output_4 = RichTextField(null=True);
	problem_note_4 = RichTextField(null=True)
	problem_pic_url_4 = models.TextField(default="-")
	problem_pic_4 = models.TextField(null=True)

	problem_name_5 = models.CharField(max_length=50,null=True)
	problem_time_limit_5 = models.CharField(max_length=50,null=True)
	problem_memory_limit_5 = models.CharField(max_length=50,null=True)
	problem_description_5 = RichTextField(null=True);
	problem_input_5 = RichTextField(null=True);
	problem_output_5 = RichTextField(null=True);
	problem_note_5 = RichTextField(null=True)
	problem_pic_url_5 = models.TextField(default="-")
	problem_pic_5 = models.TextField(null=True)
	
	def __str__(self):
		return self.contest_name
