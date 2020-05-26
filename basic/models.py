from django.db import models
from django.contrib.auth.models import User

# Модель пользователей
class Customer(models.Model):
	user = models.OneToOneField(User, null = True, blank = True, on_delete = models.CASCADE)
	name = models.CharField('Пользователь', max_length = 200, null = True)
	phone = models.CharField('Телефон', max_length = 12, null = True)
	email = models.EmailField('Эл.почта',max_length = 50, null = True)
	address = models.CharField('Адрес', max_length = 150, null = True)
	date_created = models.DateTimeField('Дата регистрации', auto_now_add = True, null = True)

	def __str__(self):
		return self.name

# Модель ресторана
class Restaurant(models.Model):
	CATEGORY = (
		('Ресторан', 'Ресторан'),
		('Закусочная', 'Закусочная'),
		('Кафе','Кафе'),
		('Кофейня','Кофейня'),
		('Кондитерская','Кондитерская'),
		('Столовая','Столовая'),
		)
	owner = models.ForeignKey(User,null = True, blank = True, on_delete = models.CASCADE)
	name = models.CharField('Имя ресторана',max_length = 100, null = True)
	phone = models.CharField('Моб. номер', max_length = 12, null = True)
	email = models.EmailField('Эл. почта', max_length = 50, null = True)
	address = models.CharField('Адрес', max_length = 150, null = True)
	categories = models.CharField('Категория',choices = CATEGORY, max_length = 30, null = True)
	paypal = models.CharField('PayPal', max_length = 150, null = True)
	restaurant_pic = models.ImageField('Изображение', upload_to = "media", default="form-img.png", null = True, blank = True)

	def __str__(self):
		return self.name

#Меню
class Menu(models.Model):
	CATEGORY = (
		('Горячие блюда', 'Горячие блюда'),
		('Холодные блюда', 'Холодные блюда'),
		('Закуски','Закуски'),
		('Десерты','Десерты'),
		('Напитки','Напитки'),
		)
	name = models.CharField('Название',max_length = 50)
	weight = models.FloatField('Вес')
	price = models.FloatField('Цена')
	category = models.CharField('Категория',choices = CATEGORY, max_length = 30)
	description = models.CharField('Описание',max_length = 300,null = True)
	restaurant = models.ForeignKey(Restaurant, null = True, on_delete = models.CASCADE)
	def __str__(self):
		return self.name

# Заказ
class Order(models.Model):

	customer = models.ForeignKey(Customer, null = True, blank= True, on_delete = models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True)
	ordered = models.BooleanField(default = False)
	
	@property
	def get_total_items(self):
		orderitems = self.ordermenu_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_total_cart(self):
		orderitems = self.ordermenu_set.all()
		total = sum([item.quantity for item in orderitems])
		return total	
	

	def __str__(self):
		return str(self.id)

class OrderMenu(models.Model):
	menu = models.ForeignKey(Menu, on_delete = models.CASCADE, null=True)
	order = models.ForeignKey(Order, on_delete = models.CASCADE, null = True)
	quantity = models.IntegerField(default = 0, null = True, blank = True)
	date_added = models.DateTimeField( auto_now_add = True)

	@property
	def get_total(self):
		total = self.menu.price * self.quantity
		return total
	
	def __str__ (self):
		return str(self.id)

