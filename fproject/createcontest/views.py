from django.shortcuts import render,get_object_or_404, redirect
from .models import Createcontest


def problemlist(request,pk):
	sitename = 'Problem List'
	contest = Createcontest.objects.filter(pk=pk)
	args = {'sitename':sitename,'contest':contest}
	return render(request,'front/problemlist.html',args)

def one(request,pk):
	sitename = 'Problem 1'
	contest = Createcontest.objects.filter(pk=pk)
	args = {'sitename':sitename,'contest':contest}
	return render(request,'front/one.html',args)

def two(request,pk):
	sitename = 'Problem 2'
	contest = Createcontest.objects.filter(pk=pk)
	args = {'sitename':sitename,'contest':contest}
	return render(request,'front/two.html',args)

def three(request,pk):
	sitename = 'Problem 3'
	contest = Createcontest.objects.filter(pk=pk)
	args = {'sitename':sitename,'contest':contest}
	return render(request,'front/three.html',args)

def four(request,pk):
	sitename = 'Problem 4'
	contest = Createcontest.objects.filter(pk=pk)
	args = {'sitename':sitename,'contest':contest}
	return render(request,'front/four.html',args)

def five(request,pk):
	sitename = 'Problem 5'
	contest = Createcontest.objects.filter(pk=pk)
	args = {'sitename':sitename,'contest':contest}
	return render(request,'front/five.html',args)
