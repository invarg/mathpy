from django.db import models

# Create your model here.
#from django.db import model

# the following lines added:
#import datetime
#from django.utils import timezone

class usr(models.Model):
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    password_confirm = models.CharField(max_length=30)
