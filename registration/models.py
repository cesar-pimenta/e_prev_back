from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, related_name='profile', editable=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    date_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
