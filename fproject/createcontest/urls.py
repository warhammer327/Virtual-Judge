from django.conf.urls import url
from . import views

urlpatterns = [
	#url(r'^$',views.firstpage,name='firstpage'),
	#url(r'^about/$',views.about,name='about'),
	url(r'^home/problemlist/$',views.problemlist,name='problemlist'),
	#url(r'^home/$',views.home,name='home'),
	url(r'^home/problemlist/one/$',views.one,name='one'),
	url(r'^home/problemlist/two/$',views.two,name='two'),
	url(r'^home/problemlist/three/$',views.three,name='three'),
	url(r'^home/problemlist/four/$',views.four,name='four'),
	url(r'^home/problemlist/five/$',views.five,name='five'),
]
