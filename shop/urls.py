from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('categorias/<int:categoria_id>/', views.mostrar_categoria, name='mostrar_categoria'),
    path('subcategorias/<int:subcategoria_id>/', views.mostrar_subcategoria, name='mostrar_subcategoria'),
    path('productos/<int:producto_id>/', views.mostrar_producto, name='mostrar_producto'),
    path('buscar_productos/', views.buscar_productos, name='buscar_productos'),
    path('logout/', views.logout_view, name='logout'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('cambiar_cantidad/<int:item_id>/<str:action>/', views.cambiar_cantidad, name='cambiar_cantidad'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('signup/', views.CustomSignupView.as_view(), name='signup'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)