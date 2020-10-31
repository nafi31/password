from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Website(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="todo",null=True)
	name = models.CharField(max_length=100)
	def __str__(self):
		return str(self.name)
class Password(models.Model):
	web  = models.ForeignKey(Website,on_delete=models.CASCADE)
	password = models.CharField(max_length=1000)
	def __str__(self):
		return str(self.password)