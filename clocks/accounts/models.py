from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField()

    def __str__(self):
        return self.user.username
