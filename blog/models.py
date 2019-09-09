from django.db import models
from django.utils import timezone
from forms.models import User
from django.urls import reverse
from user_profile.models import UserProfile



# Create your models here.
class Post(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	place = models.CharField(max_length=30)
	title = models.CharField(max_length=101,null=False,blank=False)
	price = models.IntegerField()
	description = models.TextField(max_length=1000)
	date_posted = models.DateTimeField(default = timezone.now)
	post_image = models.ImageField(upload_to='post_images')


	def __str__(self):
		return self.place

	def __str__(self):
		return self.owner

	def __str__(self):
		return self.date_posted

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-details', kwargs={"pk":self.pk}) 

	
 

