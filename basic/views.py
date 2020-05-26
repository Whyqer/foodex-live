from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse 
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
import json

from .models import *
from .decorators import *
from .forms import *
from .filters import *

'''
-----------ЧЕРНОВИК, УДАЛИТЬ ПЕРЕД ЗАЛИВОМ-----------

			----------КОНЕЦ :( ----------
'''


#-----------------------------------SETTINGS-----------------------------------

@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name = 'customer')
			user.groups.add(group)
			Customer.objects.create(
				user = user,
				name = user.first_name +' ' + user.last_name,
				email = user.email,
				)

			messages.success(request, username + ', Ваш аккаунт был успешно создан')
			return redirect('login')
		else:
			messages.info(request, 'Ошибка при вводе данных')	
	context = {'form':form}		

	return render(request, 'basic/register.html',context)

@unauthenticated_user
def restRegPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='restaurateur')
			user.groups.add(group)
			Customer.objects.create(
				user = user,
				name = user.first_name +' ' + user.last_name,
				email = user.email,
				)

			messages.success(request, username + ', Ваш аккаунт был успешно создан')
		else:
			messages.info(request, 'Ошибка при вводе данных')	
			return redirect('login')
	context = {'form':form}		

	return render(request, 'basic/restregister.html',context)

@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Ошибка в логине или пароле')	

	context = {}

	return render(request, 'basic/login.html',context)

def logoutUser(request):
	logout(request)
	return redirect('home')

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['restaurateur'])
def addRestaurant(request):

	restaurant = Restaurant(owner = request.user)
	if request.method == 'POST':
		form = RestaurantForm(request.POST, request.FILES, instance = restaurant)
		if form.is_valid():
			form.save()
			return redirect('change')
	else:
		form = RestaurantForm(instance = restaurant)
	context = {'form':form}

	return render(request,'basic/addrest.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['restaurateur'])
def redaction(request, pk):
	restaurant = Restaurant.objects.get(id = pk)
	
	if request.method == 'POST':
		form = RestaurantForm(request.POST, request.FILES, instance = restaurant)
		if form.is_valid():
			form.save()
	else:
		form = RestaurantForm(instance = restaurant)
	context = {'form':form, 'restaurant':restaurant}

	return render(request,'basic/redaction.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['restaurateur'])
def addMenu(request,pk):
	restaurant = Restaurant.objects.get(id = pk)
	menu = Menu(restaurant = restaurant)
	if request.method == 'POST':
		form = MenuForm(request.POST, request.FILES, instance = menu)
		if form.is_valid():
			form.save()
	else:
		form = MenuForm(instance = menu)

	context = {'form':form, 'restaurant':restaurant}

	return render(request,'basic/addmenu.html', context)

@login_required(login_url = 'login')
def accountSetting(request):

	customer = request.user.customer

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES, instance = customer)
		if form.is_valid():
			form.save()
	else:
		form = CustomerForm(instance = customer)
	context = {'form':form}
	return render(request,'basic/settings.html',context)

#---------------------------------END SETTINGS---------------------------------

#-----------------------------------PAGES--------------------------------------

def mainPage(request):
	mainPage = Restaurant.objects.all()
	myFilter = RestaurantFilter( request.GET, queryset = mainPage)
	context = {'mainPage':mainPage,'myFilter': myFilter}
	return render(request, 'basic/mainpage.html', context)

def restaurant(request, pk_test):
	restaurant = Restaurant.objects.get(id = pk_test)
	menus = restaurant.menu_set.all()
	myFilter = MenuFilter(request.GET, queryset = menus)
	menus = myFilter.qs



	context = {'restaurant': restaurant,'menus':menus, 'myFilter':myFilter}
	return render(request,'basic/restaurant.html', context)	


@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['restaurateur'])
def change(request):
	restaurant = Restaurant.objects.filter(owner = request.user)

	context = {'restaurant':restaurant}
	return render(request,'basic/change.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['restaurateur'])
def deleteMenu(request,pk_m):
	menu = Menu.objects.get(id=pk_m)
	if request.method == 'POST':
		menu.delete()
		return redirect('change')
	context = {'menu':menu}

	return render (request,'basic/delete.html',context)
#-----------------------------------END PAGES---------------------------------

#-----------------------------------CART--------------------------------------

@login_required(login_url = 'login')
def cart(request):
	
	customer = request.user.customer
	order, created = Order.objects.get_or_create(customer = customer, ordered = False)
	items = order.ordermenu_set.all()
	if request.method == 'POST':
		return redirect('home')

	context = {'items':items, 'customer':customer, 'order':order,'restaurant':restaurant}
	return render(request, "basic/cart.html", context)

def updatemenu(request):
	data = json.loads(request.body)
	menuId = data['menuId']
	action = data['action']

	customer = request.user.customer
	menu = Menu.objects.get(id = menuId)
	order, created = Order.objects.get_or_create(customer = customer, ordered = False)
	orderMenu, created = OrderMenu.objects.get_or_create(order = order, menu = menu)

	if action == 'add':
		orderMenu.quantity = (orderMenu.quantity + 1)
	elif action == 'remove':
		orderMenu.quantity = (orderMenu.quantity - 1)

	orderMenu.save()

	if orderMenu.quantity <= 0:
		orderMenu.delete()

	return JsonResponse('successful',safe = False)
#----------------------------------END CART-----------------------------------