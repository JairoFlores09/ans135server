import math

class Arctgx:

	def __init__(self,x,cifras):
		self.cifras = cifras
		self.x = x
		self.aproximaciones = []
		self.errores = []

	@property
	def arctgx (self):
		#Error de tolerancia
		Ess = 0.5 * (10**(2 - self.cifras));

		Ea = 100

		aproximacionActual = self.x

		n = 1

		while Ea > Ess:

			aproximacionAnterior = aproximacionActual

			aproximacionActual +=  ((-1)**n)*(self.x**(2*n + 1)/(2*n + 1))

			self.aproximaciones.append(aproximacionActual)

			Ea = abs((aproximacionActual - aproximacionAnterior)/aproximacionActual) * 100

			self.errores.append(Ea)

			n += 1

		resultado = {
			'Aproximaciones': self.aproximaciones,
			'Errores': self.errores,
		}

		return resultado