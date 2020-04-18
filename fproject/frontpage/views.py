from django.shortcuts import render,get_object_or_404, redirect
from .models import Frontpage
from createcontest.models import Createcontest
# Create your views here.



def firstpage(request):
	sitename = 'JUST'
	return render(request,'front/firstpage.html',{'sitename':sitename})

def about(request):
	sitename = 'ABOUT'
	return render(request,'front/about.html',{'sitename':sitename})

def master(request):

	return render(request,'front/master.html')

def home(request):
	sitename = 'HOME'
	contest = Createcontest.objects.all()
	args = {'sitename':sitename,'contest':contest}
	return render(request,'front/home.html',args)

def problemlist(request):
	sitename = 'Problem List'
	return render(request,'front/problemlist.html',{'sitename':sitename})

def adminpanel(request):
	sitename ='Admin Panel'
	return render(request,'back/adminpanel.html')

def contestlist(request):
	sitename = 'Contest list'
	return render(request,'back/contestlist.html')

def contest_add(request):
	if request.method == 'POST':
		contest_name = request.POST.get('contest_name')
		contest_setter = request.POST.get('contest_setter')
		contest_time = request.POST.get('contest_time')

		problem_name_1 = request.POST.get('problem_name_1')
		problem_time_limit_1 = request.POST.get('problem_time_limit_1')
		problem_memory_limit_1 = request.POST.get('problem_memory_limit_1')
		problem_description_1 = request.POST.get('problem_description_1')
		problem_input_1 = request.POST.get('problem_input_1')
		problem_output_1 = request.POST.get('problem_output_1')
		problem_note_1 = request.POST.get('problem_note_1')

		problem_name_2 = request.POST.get('problem_name_2')
		problem_memory_limit_2 = request.POST.get('problem_memory_limit_2')
		problem_time_limit_2 = request.POST.get('problem_memory_limit_2')
		problem_description_2 = request.POST.get('problem_description_2')
		problem_input_2 = request.POST.get('problem_input_2')
		problem_output_2 = request.POST.get('problem_output_2')
		problem_note_2 = request.POST.get('problem_note_2')

		problem_name_3 = request.POST.get('problem_name_3')
		problem_memory_limit_3 = request.POST.get('problem_memory_limit_3')
		problem_time_limit_3 = request.POST.get('problem_memory_limit_3')
		problem_description_3 = request.POST.get('problem_description_3')
		problem_input_3 = request.POST.get('problem_input_3')
		problem_output_3 = request.POST.get('problem_output_3')
		problem_note_3 = request.POST.get('problem_note_3')

		problem_name_4 = request.POST.get('problem_name_4')
		problem_memory_limit_4 = request.POST.get('problem_memory_limit_4')
		problem_time_limit_4 = request.POST.get('problem_memory_limit_4')
		problem_description_4 = request.POST.get('problem_description_4')
		problem_input_4 = request.POST.get('problem_input_4')
		problem_output_4 = request.POST.get('problem_output_4')
		problem_note_4 = request.POST.get('problem_note_4')

		problem_name_5 = request.POST.get('problem_name_5')
		problem_memory_limit_5 = request.POST.get('problem_memory_limit_5')
		problem_time_limit_5 = request.POST.get('problem_memory_limit_5')
		problem_description_5 = request.POST.get('problem_description_5')
		problem_input_5 = request.POST.get('problem_input_5')
		problem_output_5 = request.POST.get('problem_output_5')
		problem_note_5 = request.POST.get('problem_note_5')

		b = Createcontest(contest_name=contest_name,contest_setter=contest_setter,contest_time=contest_time,
		problem_name_1=problem_name_1,problem_memory_limit_1=problem_memory_limit_1,problem_time_limit_1=problem_time_limit_1,
		problem_description_1=problem_description_1,problem_input_1=problem_input_1,problem_output_1=problem_output_1,problem_note_1=problem_note_1,
		problem_name_2=problem_name_2,problem_memory_limit_2=problem_memory_limit_2,problem_time_limit_2=problem_time_limit_2,
		problem_description_2=problem_description_2,problem_input_2=problem_input_2,problem_output_2=problem_output_2,problem_note_2=problem_note_2,
		problem_name_3=problem_name_3,problem_memory_limit_3=problem_memory_limit_3,problem_time_limit_3=problem_time_limit_3,
		problem_description_3=problem_description_3,problem_input_3=problem_input_3,problem_output_3=problem_output_3,problem_note_3=problem_note_3,
		problem_name_4=problem_name_4,problem_memory_limit_4=problem_memory_limit_4,problem_time_limit_4=problem_time_limit_4,
		problem_description_4=problem_description_4,problem_input_4=problem_input_4,problem_output_4=problem_output_4,problem_note_4=problem_note_4,
		problem_name_5=problem_name_5,problem_memory_limit_5=problem_memory_limit_5,problem_time_limit_5=problem_time_limit_5,
		problem_description_5=problem_description_5,problem_input_5=problem_input_5,problem_output_5=problem_output_5,problem_note_5=problem_note_5,)

		b.save()

	return render(request,'back/contest_add.html')
