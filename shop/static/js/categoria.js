function agregarAlCarrito(productoId) {
    fetch(`/agregar_al_carrito/${productoId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}', // Agregar el token CSRF a la solicitud
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        // Actualizar la cantidad en el carrito en el botón
        const badge = document.querySelector('.badge');
        badge.textContent = data.cantidad;
    });
}

// Manejar el clic en el botón "Agregar al carrito"
const agregarCarritoButtons = document.querySelectorAll('.agregar-carrito');
agregarCarritoButtons.forEach(button => {
    button.addEventListener('click', function(event) {
        event.preventDefault();
        const productoId = this.dataset.productoId;
        agregarAlCarrito(productoId);
    });
});