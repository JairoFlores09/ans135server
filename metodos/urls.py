from django.urls import path
from . import views

urlpatterns = [
	#url's para métodos de la unidad 1
	path('unidad1/sin/', views.sinx, name='Sinx'),
	path('unidad1/cos/', views.cosx, name='Cosx'),
	path('unidad1/cosh/', views.coshx, name='Coshx'),
	path('unidad1/arctgx/',views.arctgx, name='Arctgx'),
	path('unidad1/fraccion/',views.fraccion, name='Fraccion'),
	path('unidad1/ln/', views.logaritmo, name="Logaritmo"),
	path('unidad1/arcsin/', views.arcsinx, name="Arcsinx"),
	path('unidad1/sinh/', views.sinhx, name="Sinhx"),
]