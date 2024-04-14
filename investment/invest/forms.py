from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import InvestBeginner,InvestProfessional,InvestPromo, InvestRep,InvestFinale

class BeginnerForm(forms.ModelForm):
    class Meta:
        model = InvestBeginner
        fields =["coin","amount"]

        def save(self, **kwargs):
        	user = kwargs.pop('user')
        	instance = super(InvestBeginner, self).save(**kwargs)
        	instance.user = InvestBeginner.objects.get(user=user) 
        	instance.save()
        	return instance

class ProfessionalForm(forms.ModelForm):
    class Meta:
        model = InvestProfessional
        fields =["coin","amount"]

        def save(self, **kwargs):
        	user = kwargs.pop('user')
        	instance = super(InvestProfessional, self).save(**kwargs)
        	instance.user = InvestProfessional.objects.get(user=user) 
        	instance.save()
        	return instance

class PromoForm(forms.ModelForm):
    class Meta:
        model = InvestPromo
        fields =["coin","amount"]

        def save(self, **kwargs):
        	user = kwargs.pop('user')
        	instance = super(InvestPromo, self).save(**kwargs)
        	instance.user = InvestPromo.objects.get(user=user) 
        	instance.save()
        	return instance

class RepForm(forms.ModelForm):
    class Meta:
        model = InvestRep
        fields =["coin","amount"]

        def save(self, **kwargs):
        	user = kwargs.pop('user')
        	instance = super(InvestRep, self).save(**kwargs)
        	instance.user = InvestRep.objects.get(user=user) 
        	instance.save()
        	return instance

class FinaleForm(forms.ModelForm):
    class Meta:
        model = InvestFinale
        fields =["coin","amount"]

        def save(self, **kwargs):
        	user = kwargs.pop('user')
        	instance = super(InvestFinale, self).save(**kwargs)
        	instance.user = InvestFinale.objects.get(user=user) 
        	instance.save()
        	return instance

class SignUpForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length=60)
	last_name = forms.CharField(max_length=60)

	class Meta:
		model = User
		fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
	remember_me = forms.BooleanField(required=False)



class EmailForm(forms.Form):
	name = forms.CharField(max_length=60)
	email = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea)