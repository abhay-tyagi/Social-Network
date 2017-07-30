# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

Gender_choice = (
	('Select gender', '-'),
	('Male', 'Male'),
	('Female', 'Female'),
	)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	fullname = models.CharField(max_length=50)
	gender = models.CharField(max_length=6, choices = Gender_choice)  #No LGBT
	profession = models.CharField(max_length=20)
	#friends = models.IntegerField(default=0) For later

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField(default=datetime.date.today)
	content = models.TextField()
	title = models.CharField(max_length=50, default="my_post")
	like_count = models.IntegerField(default=0)
	time = models.TimeField(default=datetime.datetime.now)

	def __str__(self):
		return self.title

class Like(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
	by = models.ForeignKey(User, on_delete=models.CASCADE)
	to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")


class Comment(models.Model):
	content = models.TextField()
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
	by = models.ForeignKey(User, on_delete=models.CASCADE)
	to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
	date = models.DateField(default=datetime.date.today)	
	time = models.TimeField(default=datetime.datetime.now)

	def __str__(self):
		return self.content


