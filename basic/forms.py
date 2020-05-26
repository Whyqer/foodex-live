from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username',
		 'first_name', 
		 'last_name', 
		 'email', 
		 'password1', 
		 'password2']

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']


class RestaurantForm(ModelForm):
	class Meta:
		model = Restaurant
		fields = '__all__'
		exclude = ['owner']


class MenuForm(ModelForm):
	class Meta:
		model = Menu
		fields = '__all__'
		exclude = ['restaurant']		