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
	return render(request,'front/home.html',{'sitename':sitename})

def problemlist(request):
	sitename = 'Problem List'
	return render(request,'front/problemlist.html',{'sitename':sitename} )
