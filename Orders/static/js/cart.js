// Update item quantity
function updateQuantity(itemId, change) {
    let quantityElement = document.getElementById(`quantity-${itemId}`);
    let currentQuantity = parseInt(quantityElement.innerText);
    let newQuantity = currentQuantity + change;

    if (newQuantity < 1) return;

    quantityElement.innerText = newQuantity;
    console.log(itemId, newQuantity);
    updateItemTotal(itemId, newQuantity);
    updateCartTotal();
}

// Remove item from cart
function removeItem(itemId) {
    let itemElement = document.querySelector(`.cart-item[data-id='${itemId}']`);
    if (itemElement) itemElement.remove();
    updateCartTotal();
}

// Update individual item total price
function updateItemTotal(itemId, quantity) {
    let price = document.getElementById(`item-price-${itemId}`).innerHTML.slice(1);
    price = parseFloat(price);
    let itemTotal = price * quantity;
    let itemTotalElement = document.getElementById(`item-total-${itemId}`);
    itemTotalElement.innerText = `$${itemTotal.toFixed(2)}`;

}

// Update cart total price
function updateCartTotal() {
    let itemTotalElements = document.querySelectorAll('.item-total-price');
    let cartTotal = 0;

    itemTotalElements.forEach(itemTotal => {
        console.log(itemTotal.innerText);
        cartTotal += parseFloat(itemTotal.innerText.slice(1));
    });

    document.getElementById('cart-total').innerText = `$${cartTotal.toFixed(2)}`;
    console.log(cartTotal);
}


// API call demo
function getItems() {
    fetch('http://dummy.restapiexample.com/api/v1/employees')
        .then(response => response.json())
        .then(data => console.log(data));
}

// Explains how to use fetch API
// https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch

// POST request example
function addItem() {
    fetch('http://dummy.restapiexample.com/api/v1/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: 'test',
            salary: '123',
            age: '23'
        })
    })
        .then(response => response.json())
        .then(data => console.log(data));
}