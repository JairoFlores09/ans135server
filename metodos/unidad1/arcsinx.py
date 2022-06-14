from math import factorial,pow

class Arcsinx:
	def __init__(self, cifras, x):
		self.cifras = cifras
		self.x = x
		self.aproximaciones = []
		self.errores = []


	@property
	def arcsinx(self):
		#Error de tolerancia
		Ess = 0.5 * (10**(2 - self.cifras)); 

		Ea = 100

		aproximacionActual = self.x 

		n = 1
		while Ea > Ess:
			self.aproximaciones.append(aproximacionActual)

			aproximacionAnterior = aproximacionActual

			aproximacionActual += (factorial(2*n)/pow((pow(2,n)*factorial(n)),2))*(pow(self.x,(2*n + 1))/(2*n + 1))

			Ea = abs((aproximacionActual - aproximacionAnterior)/aproximacionActual)*100

			self.errores.append(Ea)

			n += 1

		resultado = {
			'Aproximaciones': self.aproximaciones,
			'Errores': self.errores
		}

		return resultado