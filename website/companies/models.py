from django.db import models

class Stock(models.Model):
	ticker=models.CharField(max_length=10)
	opening=models.FloatField()
	closing=models.FloatField()
	volume=models.IntegerField()

	def __str__(self):
		return self.ticker