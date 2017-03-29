from django.db import models

# Create your models here.

class UserAndPass(models.Model):
	user_name = models.CharField(max_length=30)
	user_pass = models.CharField(max_length=30)

