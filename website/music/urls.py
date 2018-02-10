from django.conf.urls import url
from . import views

app_name='music' # NAMESPACING using this will allow us to specify which view.datail we want to call in case there are other apps using detail 

urlpatterns=[
# /music/
	url(r'^$',views.IndexView.as_view(), name='index'),

	url(r'register/$',views.UserFormView.as_view(), name='register'),
#music/<album_id>/
	url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),	
#music/album/add/
	url(r'album/add/$',views.AlbumCreate.as_view(),name='album-add'),

	url(r'album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name='album-update'),

	url(r'album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(),name='album-delete'),

]