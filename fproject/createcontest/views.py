from django.shortcuts import render,get_object_or_404, redirect
from .models import Createcontest


def problemlist(request,pk):
	sitename = 'Problem List'
	contest = Createcontest.objects.filter(pk=pk)
	args = {'sitename':sitename,'contest':contest}
	return render(request,'front/problemlist.html',args)

def problem(request,pk):
	sitename = 'Problem'
	contest = Createcontest.objects.filter(pk=pk)
	return render(request,'front/problem.html')
