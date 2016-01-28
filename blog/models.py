from django.db import models
from django.utils import timezone

class Post(models.Model): # Post = model name, class to define object, models.Model means that 'object' Post is a Django Model(to be saved into database)
	author = models.ForeignKey('auth.User') # models.ForeignKey link to another model
	title = models.CharField(max_length=200)# models.CharField = how we define text with limited set of characters
	text = models.TextField()# models.TextField this is for long text without a limit (good for article in blog content post
	created_date = models.DateTimeField(default=timezone.now) # models.DateTimeField = date and time field as input 
	published_date = models.DateTimeField(blank=True, null=True) # same as above

	def publish(self): # function to do something inside the model/object
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title





