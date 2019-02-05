from django.db.models.signals import post_save #this signal gets fired after an object is saved
from django.contrib.auth.models import User #User model is the signal sender
#we also need to create a receiver
from django.dispatch import receiver
#we also import P rofile from our models since we'll be creating profile in our function
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender,  instance, created, **kwargs): #now we have a create profile function that we want to run everytime a user is created
    if created:
        Profile.objects.create(user=instance)

#another function to save profile
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
