from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    register_date = models.DateField(auto_now=True)
    adress_place = models.CharField(max_length=80, null=True, blank=True)
    adress_number = models.IntegerField(null=True, blank=True)
    adress_complement = models.CharField(max_length=160, null=True, blank=True)
    adress_neighborhood = models.CharField(max_length=50, null=True, blank=True)
    adress_city = models.CharField(max_length=50, null=True, blank=True)
    adress_country = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    @property
    def username(self):
        return f'{self.user.username}'

    @property
    def email(self):
        return f'{self.user.email}'    

    def __str__(self):
        return str(self.user)
    
    def __repr__(self):
        return self.user
        
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()