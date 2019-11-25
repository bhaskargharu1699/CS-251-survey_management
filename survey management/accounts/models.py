from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.DO_NOTHING,)
	descriptiion = models.CharField(max_length=100,default='')
	city = models.CharField(max_length=100,default='')
	website = models.URLField(default = '')
	phone = models.IntegerField(default = 0)

def create_profile(sender,**kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
def delete_user(sender, instance=None, **kwargs):
    try:
        instance.user
    except User.DoesNotExist:
        pass
    else:
        instance.user.delete()
post_delete.connect(delete_user, sender=UserProfile,dispatch_uid='website.models.user_deleted')
