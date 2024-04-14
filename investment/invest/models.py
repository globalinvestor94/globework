from django.db import models
import random
from django.utils import timezone
from django.conf import settings

CHOICES = [
	('Select Coin','Select Coin'),
	('Bitcoin','Bitcoin'),
	('Ethurum','Ethurum'),
	('BnB','BnB'),
	('USDT Tron','USDT Tron'),
	('USDT ERC20','USDT ERC20'),
	]


STATUS = [
	('Pending','Pending'),
	('Processing','Processing'),
	('Rewarded','Rewarded'),
	]


class learnMore(models.Model):
	description = models.TextField()
	pictures =  models.ImageField(upload_to='Pictures/', blank=True)
	descriptions = models.TextField()
	date = models.DateTimeField(default=timezone.now)


class About(models.Model):
	title = models.CharField(max_length=200)
	preview_text = models.CharField(max_length=200)
	body_text = models.TextField()
	date = models.DateTimeField(default=timezone.now)


class Testimony(models.Model):
	name = models.CharField(max_length=200)
	testimony = models.CharField(max_length=500)
	pictures =  models.ImageField(upload_to='Pictures/', blank=True)
	date = models.DateTimeField(default=timezone.now)


class InvestBeginner(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	coin = models.CharField(max_length=100, choices=CHOICES, default='Select Coin')
	amount = models.IntegerField() 
	status = models.CharField(max_length=100, choices=STATUS, default='Pending')
	def __str__(self):
		return self.user.username

	def beginner_amount (self):
		return self.amount * 5 /100 + self.amount


class InvestProfessional(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	coin = models.CharField(max_length=100, choices=CHOICES, default='Select Coin')
	amount = models.IntegerField() 
	status = models.CharField(max_length=100, choices=STATUS, default='Pending')
	def __str__(self):
		return self.user.username

	def professional_amount (self):
		return self.amount * 8 /100 + self.amount


class InvestPromo(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	coin = models.CharField(max_length=100, choices=CHOICES, default='Select Coin')
	amount = models.IntegerField() 
	status = models.CharField(max_length=100, choices=STATUS, default='Pending')
	def __str__(self):
		return self.user.username

	def promo_amount (self):
		return self.amount * 11 /100 + self.amount


class InvestRep(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	coin = models.CharField(max_length=100, choices=CHOICES, default='Select Coin')
	amount = models.IntegerField() 
	status = models.CharField(max_length=100, choices=STATUS, default='Pending')
	def __str__(self):
		return self.user.username

	def rep_amount (self):
		return self.amount * 14 /100 + self.amount


class InvestFinale(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	coin = models.CharField(max_length=100, choices=CHOICES, default='Select Coin')
	amount = models.IntegerField() 
	status = models.CharField(max_length=100, choices=STATUS, default='Pending')
	def __str__(self):
		return self.user.username

	def finale_amount (self):
		return self.amount * 17 /100 + self.amount
# Create your models here.

