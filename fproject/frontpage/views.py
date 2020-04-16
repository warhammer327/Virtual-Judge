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
