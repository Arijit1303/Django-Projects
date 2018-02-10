from django.views import generic
from .models import Album
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy #used by delete
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import View
from .models import Album
from .forms import UserForm

class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name='all_albums'

	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model = Album
	template_name ='music/detail.html'

class AlbumCreate(CreateView):
	model = Album
	fields = ['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
	model = Album
	fields = ['artist','album_title','genre','album_logo']	

class AlbumDelete(DeleteView):
	model = Album 
	success_url=reverse_lazy('music:index')

class UserFormView(View):
	form_class = UserForm
	template_name='music/registration_form.html'
	#Displays blank form
	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})
	#process form data 	
	def post(self,request):
		form = self.form_class(request.POST)
		
		if form.is_valid():
			
			user=form.save(commit=False)

			#cleaned (Unified) data

			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#returns User objects if credentials are correct


			user=authenticate(username=username,password=password)

			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('music:index')

		return render(request,self.template_name,{'form':form})	

"""from django.http import HttpResponse, Http404
from .models import Album,Song # to list view all the albums
#OBS:from django.template import loader #importing template
from django.shortcuts import render,get_object_or_404

def index(request):
	#OBS:return HttpResponse("<h1>Welcome back !</h1>")
	all_albums=Album.objects.all()
	#OBS:template =loader.get_template('music/index.html')
	#OBS:context={'all_albums':all_albums,}4
	return render(request,'music/index.html',{'all_albums':all_albums})

	OBS:html=''
	for album in all_albums:
		url='/music/'+str(album.id)+'/'
		html +='<a href="' + url + '">'+str(album.album_title)+ '</a><br>'
	
	#OBS:return HttpResponse(template.render(context,request))


def detail(request,album_id):
	album = get_object_or_404(Album, pk=album_id)
	return render(request,'music/detail.html',{'album':album})
	#OBS:return HttpResponse("<h2>Details for album id "+ str(album_id) +"</h2>")

	 OBS try:
		album=Album.objects.get(pk=album_id)
	   except Album.DoesNotExist:
		raise Http404("Album does not exist")
	

def favourite(request,album_id):
	album = get_object_or_404(Album, pk=album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])
	except(KeyError, Song.DoesNotExist):
		return render(request,'music/detail.html',{
			'album':album,
			'error_message':"Invalid Song"
			})
	else:
		selected_song.is_favourite = True						
		selected_song.save()
	return render(request,'music/detail.html',{'album':album})		"""