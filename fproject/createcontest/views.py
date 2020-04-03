from django.shortcuts import render,get_object_or_404, redirect
from .models import Createcontest



def problemlist(request):
	sitename = 'Problem List'
	return render(request,'front/problemlist.html',{'sitename':sitename})

def one(request):
	sitename = 'Problem 1'
	contest = Createcontest.objects.all()
	args = {'sitename':sitename,'contest':contest}
	return render(request,'front/one.html',args)


def two(request):
	sitename = 'Problem 2'
	return render(request,'front/two.html',{'sitename':sitename})

def three(request):
	sitename = 'Problem 3'
	return render(request,'front/three.html',{'sitename':sitename})

def four(request):
	sitename = 'Problem 4'
	return render(request,'front/four.html',{'sitename':sitename})

def five(request):
	sitename = 'Problem 5'
	return render(request,'front/five.html',{'sitename':sitename})
