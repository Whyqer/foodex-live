function completeOrder(){
	 var url = "/checkout/"

	fetch(url, {
 		method:'POST',
	 	headers:{
	 		'Content-type':'application/json',
	 		'X-CSRFToken':csrftoken,
	 	},
	 	body:JSON.stringify({'menuId':menuId})
	})
}

// Render the PayPal button into #paypal-button-container
paypal.Buttons({
    // Set up the transaction
    createOrder: function(data, actions) {
        return actions.order.create({
            purchase_units: [{ 
                amount: {
                    value: total
                }
            }]
        });
    },

            // Finalize the transaction
    onApprove: function(data, actions) {
        return actions.order.capture().then(function(details) {
            // Show a success message to the buyer
            completeOrder()
            alert('Transaction completed by ' + details.payer.name.given_name + '!');
        });
    }
}).render('#paypal-button-container');