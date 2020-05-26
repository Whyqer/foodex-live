import django_filters

from .models import *

class MenuFilter(django_filters.FilterSet):
	class Meta:
		model = Menu
		fields = ['category']

class RestaurantFilter(django_filters.FilterSet):
	class Meta:
		model = Restaurant
		fields = ['categories']