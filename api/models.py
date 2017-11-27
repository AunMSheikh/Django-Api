from django.db import models

# Create your models here.

class AppUser(models.Model):
    """ This class represents the application user data """
    username = models.CharField(max_length=255, blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False)
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=50, blank=False)

    def __str__ (self):
        return (self.username + " is: " + self.name)