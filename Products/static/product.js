function addToCart(product_id)
{
    const base_url = window.location.origin;
    const url = base_url + '/orders/add-to-cart/';
    access_token = localStorage.getItem('access');
    if(access_token){
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + access_token
            },
            body: JSON.stringify({'product_id': product_id})
        })
        .then(response => response.json())
        .then(data => {
            if(data['message'] == 'Product added to cart'){
                alert('Product added to cart');
            }
            else{
                // show error message
                alert(data['message']);
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }
    else{
        alert('Please login to add product to cart');
        // Redirect to login page
        window.location.href = base_url + 'users/signin/';
    }

}

// why do we stringify the data before sending it to the server?
// The fetch API does not accept a JSON object as a body. It only accepts a string or a FormData object.