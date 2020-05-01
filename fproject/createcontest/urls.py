from django.conf.urls import url
from . import views

urlpatterns = [
	#url(r'^$',views.firstpage,name='firstpage'),
	#url(r'^about/$',views.about,name='about'),
	url(r'^home/(?P<pk>\d+)/$',views.problemlist,name='problemlist'),
	#url(r'^home/(?P<pk>\d+)/(?P<id>\d+)/$',views.problemdetail,name='problemdetail'),
	#url(r'^home/$',views.home,name='home'),


]
