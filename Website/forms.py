from django.contrib.auth.models import User
from django import forms

class Regform(forms.ModelForm):
	firstname = forms.CharField(label='First Name', max_length=50, required = True)
	lastname = forms.CharField(label='Last Name', max_length=50, required = True)
	email = forms.EmailField(label='Email', required = True)
	username = forms.CharField(label='Username', max_length=50, required = True)
	password = forms.CharField(widget=forms.PasswordInput(), required = True)

	class Meta:
		model = User
		fields = ('firstname', 'lastname', 'email', 'username', 'password')

class Logform(forms.Form):
	username = forms.CharField(label='Username', max_length=50, required = True)
	password = forms.CharField(widget=forms.PasswordInput(), required = True)
