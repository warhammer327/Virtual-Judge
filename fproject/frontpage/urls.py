from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.firstpage,name='firstpage'),
	url(r'^about/$',views.about,name='about'),
	url(r'^master/$',views.master,name='master'),
	url(r'^home/$',views.home,name='home'),
	url(r'^adminpanel/$',views.adminpanel,name='adminpanel'),
	url(r'^adminpanel/contestlist/$',views.contestlist,name='contestlist'),
	url(r'^adminpanel/contest_add/$',views.contest_add,name='contest_add'),
	url(r'^adminpanel/contestlist/del/(?P<pk>\d+)/$',views.contest_del,name='contest_del'),
	url(r'^adminpanel/contestlist/edit/(?P<pk>\d+)/$',views.contest_edit,name='contest_edit'),
	url(r'^adminlogin/$',views.adminlogin,name='adminlogin'),
	url(r'^adminlogout/$',views.adminlogout,name='adminlogout'),
]
