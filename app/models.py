from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class UserKeys(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phrase = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username
    
class UserProfile(models.Model):

    profile_is_completed = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name='profile', default=None )
    avatar = models.ImageField(default='avartar/default_avatar.png', upload_to='avatar/', blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    organisation = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    zipcode = models.CharField(max_length=30, blank=True, null=True)

    


    def __str__(self):
        return "{0}".format(self.user.username)
    
   
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'userprofile'):
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()