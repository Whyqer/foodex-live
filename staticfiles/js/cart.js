var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var menuId = this.dataset.menu
		var action = this.dataset.action
		console.log('menuId:', menuId, 'action:', action)
		console.log('USER:', user)

		if (user == 'AnonymousUser'){
			console.log('error')
			//addCookieItem(menuId, action)
		}else{
			updateUserOrder(menuId, action)
		}
	})
}



function updateUserOrder(menuId, action){
	var url = '/update_menu/'
	var csrftoken = getCookie('csrftoken');

	fetch(url, {
		method:'POST',
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken': csrftoken,
		},
		body:JSON.stringify({
			'menuId':menuId, 'action':action,
		})
	})

	.then((response) =>{
		return response.json()
	})

	.then((data) =>{
		console.log('data:', data)
		location.reload()
	})
}

/*
function addCookieItem(mmenuId, action){
	if (action == 'add'){
		if (cart[menuId] == undefined){
		cart[menuId] = {'quantity':1}

		}else{
			cart[menuId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[menuId]['quantity'] -= 1

		if (cart[menuId]['quantity'] <= 0){
			delete cart[menuId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()
}

*/ 