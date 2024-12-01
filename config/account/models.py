from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    country = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    street = models.CharField(max_length=100)

    def __str__(self):
        return f'Profile of {self.user.username}'