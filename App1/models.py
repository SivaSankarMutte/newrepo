from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Questions(models.Model):
	q1=models.CharField(max_length=500)
	opt1=models.CharField(max_length=100)
	opt2=models.CharField(max_length=100)
	opt3=models.CharField(max_length=100)
	opt4=models.CharField(max_length=100)
	ans=models.CharField(max_length=1)
 
class User(AbstractUser):
 	#name=models.CharField(max_length=100)
 	clg=models.CharField(max_length=200,null=True)
 	regdno=models.CharField(max_length=100,null=True)
 	rollno=models.IntegerField(null=True)
 	email=models.CharField(max_length=150,null=True)
 	g=[('Male','Male'),('Female','Female')]
 	gender=models.CharField(max_length=10,choices=g,default="Male")
 	b=[('CSE','CSE'),('ECE','ECE'),('MECH','MECH'),('CIVIL','CIVIL'),('EEE','EEE'),('E&I','E&I')]
 	branch=models.CharField(max_length=50,choices=b,default="CSE")
 	t=[(1,'Guest'),(2,'Professor'),(3,'Student')]
 	role=models.IntegerField(choices=t,default=1)
 	uimg=models.ImageField(upload_to='Profilepics/',default='dummyProfile.png')
 	
class Marksheet(models.Model):
	name=models.CharField(max_length=100,default="")
	regdno=models.CharField(max_length=100,default="")
	marks=models.IntegerField(default=0)

class Rolereq(models.Model):
	f=[(2,'Professor'),(3,'Student')]
	rltype=models.IntegerField(choices=f)
	pfe=models.ImageField(upload_to='Rolereqpics/',default='dummyProfile.png')
	is_checked=models.BooleanField(default=False)
	uname=models.CharField(max_length=50)
	ud=models.OneToOneField(User,on_delete=models.CASCADE)

