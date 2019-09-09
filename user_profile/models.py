from django.db import models
from forms.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here. 
class UserProfileManager(models.Manager):
	def profile_update(request,image):
		profile_update_obj = self.model(image= image)



class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	image = models.ImageField(default='default.jpg',upload_to='profile_pics')	

	def __str__(self):
		return f'{self.user.full_name}'

	def save(self,*args,**kwargs):
		super(UserProfile,self).save(*args,**kwargs)



		img = Image.open(self.image.path)

		if img.height > 200 or img.width > 200:
		    output_size = (200,200)
		    img.thumbnail(output_size)
		    img.save(self.image.path)

		    
	objects = UserProfileManager()

#signal.py
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)
		post_save.connect(create_profile, sender = User)