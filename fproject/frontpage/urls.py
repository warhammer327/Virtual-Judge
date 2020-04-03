from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.firstpage,name='firstpage'),
	url(r'^about/$',views.about,name='about'),
	url(r'^master/$',views.master,name='master'),
	url(r'^home/$',views.home,name='home'),
]
