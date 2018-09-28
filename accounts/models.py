from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# how to do custom filter in queryset for frequently used query
class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager,self).get_queryset().filter(city='Lagos')

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descriptions = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    website = models.URLField(default="")
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)
    objects = models.Manager()
    lagos = UserProfileManager()
    def __str__(self):
        return self.user.username

# it will create this table when a user register 
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
      