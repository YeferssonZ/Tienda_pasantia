# context_processors.py

from .models import *

def categorias_subcategorias(request):
    categorias = Categoria.objects.all()
    subcategorias = Subcategoria.objects.all()
    return {'categorias': categorias, 'subcategorias': subcategorias}

def carrito_cantidad(request):
    cantidad_productos = 0
    if request.user.is_authenticated:
        # Obtener la cantidad desde la base de datos si el usuario está logueado
        try:
            carrito = Carrito.objects.get(usuario=request.user)
            cantidad_productos = carrito.itemcarrito_set.aggregate(total_cantidad=models.Sum('cantidad'))['total_cantidad']
            if cantidad_productos is None:
                cantidad_productos = 0
        except Carrito.DoesNotExist:
            pass
    else:
        carrito_id = request.session.get('carrito_id')  # Cambiar esta línea
        if carrito_id:
            try:
                carrito = Carrito.objects.get(id=carrito_id)
                cantidad_productos = carrito.itemcarrito_set.aggregate(total_cantidad=models.Sum('cantidad'))['total_cantidad']
            except Carrito.DoesNotExist:
                pass
        
    return {'carrito_cantidad': cantidad_productos}