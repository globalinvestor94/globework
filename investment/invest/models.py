from django.db import models
import random
from django.utils import timezone
from django.conf import settings
from .utils import generate_ref_code
from django.contrib.auth.models import User


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


class UserReferal (models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="referrals")
	code = models.CharField(max_length=12, blank=True)
	recommeded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="referred_by")
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.username}"

	def get_recommended_profiles(self):
		query = UserReferal.objects.all()
		my_rec = [ur for ur in query if ur.recommeded_by == self.user]
		return my_rec


	def save(self, *args, **kwargs):
		if self.code == "":
			code = generate_ref_code()
			self.code = code
		super().save(*args, **kwargs)
