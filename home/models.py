from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length = 1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.post) > 80:
            return self.post[0:80] + " .............."
        else:
            return self.post

class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE, null=True)

    @classmethod
    def make_friend(cls,  current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls,  current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)
