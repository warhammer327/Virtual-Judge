from django.shortcuts import render,get_object_or_404, redirect
from .models import Createcontest



def problemlist(request):
	sitename = 'Problem List'
	contest = Createcontest.objects.get(id=self.id)
	args = {'sitename':sitename,'contest':contest}
	return render(request,'front/problemlist.html',args)

def one(request):
	sitename = 'Problem 1'
	contest = Createcontest.objects.get(id=self.id)
	args = {'sitename':sitename,'contest':contest}
	return render(request,'front/one.html',args)


def two(request):
	sitename = 'Problem 2'
	contest = Createcontest.objects.all()
	args = {'sitename':sitename,'contest':contest}
	return render(request,'front/two.html',args)

def three(request):
	sitename = 'Problem 3'
	contest = Createcontest.objects.all()
	args = {'sitename':sitename,'contest':contest}
	return render(request,'front/three.html',args)

def four(request):
	sitename = 'Problem 4'
	contest = Createcontest.objects.all()
	args = {'sitename':sitename,'contest':contest}
	return render(request,'front/four.html',args)

def five(request):
	sitename = 'Problem 5'
	contest = Createcontest.objects.all()
	args = {'sitename':sitename,'contest':contest}
	return render(request,'front/five.html',args)
