from django.db import models
from django.views.generic.edit import CreateView
from django.urls import reverse
# Red pk1
class Album(models.Model):
	artist = models.CharField(max_length=250)
	album_title=models.CharField(max_length=500)
	genre=models.CharField(max_length=500)
	album_logo=models.FileField()
	#Dunder string to display objects in the database
	def get_absolute_url(self):
		return reverse('music:detail',kwargs={'pk':self.pk})
		#here we are redirectcing the form in detail view

	def __str__(self):
		return self.album_title+ ' - ' +self.artist	

class Song(models.Model):
	album=models.ForeignKey(Album,on_delete=models.CASCADE)
	file_type=models.CharField(max_length=10)
	song_title=models.CharField(max_length=250)

	def __str__(self):
		return self.song_title+ ' - ' +self.file_type	




