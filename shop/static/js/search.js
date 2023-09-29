const searchInput = document.getElementById('search-input');
    const suggestionsContainer = document.getElementById('suggestions-container');

    searchInput.addEventListener('input', () => {
        const searchText = searchInput.value.trim();
        if (searchText === '') {
            suggestionsContainer.innerHTML = '';
            return;
        }

        // Realizar la solicitud AJAX al servidor
        const url = `/productos/buscar_productos/?q=${encodeURIComponent(searchText)}`;
        fetch(url)
            .then(response => response.json())
            .then(data => {
                const suggestions = data.map(producto => `<div>${producto.nombre} (S/. ${producto.precio})</div>`).join('');
                suggestionsContainer.innerHTML = suggestions;
            })
            .catch(error => {
                console.error('Error al obtener las sugerencias:', error);
            });
    });