from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# =========== UNIDAD 1 ==========
from metodos.unidad1.sinx import Sinx
from metodos.unidad1.cosx import Cosx
from metodos.unidad1.coshx import Coshx
from metodos.unidad1.arctgx import Arctgx
from metodos.unidad1.fraccion import Fraccion
from metodos.unidad1.sinhx import Sinhx


@api_view(['POST'])
def sinx(request):
	resultado = {}
	try:
		cifras = int(request.data['cifras'])
		if cifras < 1:
			resultado['error'] = 'Ingresa un número positivo en las cifras significativas'
			return Response(resultado,status = status.HTTP_400_BAD_REQUEST)
		x = float(request.data['x'])
		resultado = Sinx(cifras,x).sinx
		return Response(resultado, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingreses sean válidos'
		return Response(resultado,status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def cosx(request):
	resultado = {}
	try:
		cifras = int(request.data['cifras'])
		if cifras < 1:
			resultado['error'] = 'Ingrese un número positivo en las cifras significativas'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		x = float(request.data['x'])
		resultado = Cosx(x,cifras).cosx
		return Response(resultado, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingreses sean válidos'
		return Response(resultado, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def coshx(request):
	resultado = {}
	try:
		cifras = int(request.data['cifras'])
		if cifras < 1:
			resultado['error'] = 'Ingrese un número positivo en las cifras significativas'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		x = float(request.data['x'])
		resultado = Coshx(x,cifras).coshx
		return Response(resultado, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingreses sean válidos'
		return Response(resultado, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def arctgx(request):
	resultado = {}
	try:
		cifras = int(request.data['cifras'])
		if cifras < 1:
			resultado['error'] = 'Ingrese un número positivo en las cifras significativas'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		x = float(request.data['x'])

		if x > -1 and x < 1:
			resultado = Arctgx(x,cifras).arctgx
			return Response(resultado, status=status.HTTP_200_OK)
		else:
			resultado['error'] = "El valor de x debe pertenecer al intervalo ]-1;1["
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingreses sean válidos'
		return Response(resultado, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def fraccion(request):
	resultado = {}
	try:
		cifras = int(request.data['cifras'])
		if cifras < 1:
			resultado['error'] = 'Ingrese un número positivo en las cifras significativas'
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
		x = float(request.data['x'])

		if x > -1 and x < 1:
			resultado = Fraccion(x,cifras).fraccion
			return Response(resultado, status=status.HTTP_200_OK)
		else:
			resultado['error'] = "El valor de x debe pertenecer al intervalo ]-1;1["
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingreses sean válidos'
		return Response(resultado, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logaritmo(request):
	resultado = {}
	resultado['error'] = 'Este método aún no está en funcionamiento! Regrese más tarde :)'
	return Response(resultado, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def sinhx(request):
	resultado = {}
	try:
		x = request.data['x']
		cifras = int(request.data['cifras'])
		if cifras < 1:
			resultado['error'] = "Ingrese un número positivo en las cifras significativas"
			return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

		respuesta = Sinhx(cifras, x).sinhx
		return Response(respuesta, status=status.HTTP_200_OK)
	except Exception:
		resultado['error'] = 'Asegurate que todos los datos que ingresaste sean válidos'
		return Response(resultado, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def arcsinx(request):
	resultado = {}
	resultado['error'] = 'Este método aún no está en funcionamiento! Regrese más tarde :)'
	return Response(resultado, status=status.HTTP_404_NOT_FOUND)
