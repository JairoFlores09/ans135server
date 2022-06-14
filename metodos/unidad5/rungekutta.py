from sympy import *
import numpy as np

class RungeKutta:
	def __init__(self, f, x0, y0, xf, h = 0, n = 0):
		self.f = sympify(f.replace("^","**"))
		self.x0 = sympify(x0)
		self.y0 = sympify(y0)
		self.xf = sympify(xf)
		self.h = h
		self.n = n

	def eval(self, valorX, valorY):
		x, y = symbols("x y")
		return self.f.subs([(x, float(valorX)), (y, float(valorY))])


	@property
	def rungekutta4(self):
		if self.h == 0 and self.n == 0:
			return "666"

		if self.h == 0:
			self.h = (float(self.xf) - float(self.x0))/self.n

		if self.n == 0:
			self.n = (float(self.xf) - float(self.x0))/self.h

		x = list(np.linspace(float(self.x0), float(self.xf), int(self.n+1)))

		k1 = float(self.eval(self.x0, self.y0))
		k2 = float(self.eval(self.x0 + (self.h/2),self.y0 + ((self.h * k1)/2)))
		k3 = float(self.eval(self.x0 + (self.h/2),self.y0 + ((self.h * k2)/2)))
		k4 = float(self.eval(self.x0 + self.h,self.y0 + (self.h*k3)))

		yf = []
		yf.append(self.y0)
		#primera iteracion de runge kutta
		yf.append(yf[0] + ((self.h/6)*(k1 + 2*k2 + 2*k3 + k4)))

		for i in range(2, len(x)):
			k1 = float(self.eval(x[i-1], yf[i-1]))
			k2 = float(self.eval(x[i-1] + (self.h/2),yf[i-1] + ((self.h * k1)/2)))
			k3 = float(self.eval(x[i-1] + (self.h/2),yf[i-1] + ((self.h * k2)/2)))
			k4 = float(self.eval(x[i-1] + self.h,yf[i-1] + (self.h*k3)))

			yf.append(yf[i-1] + ((self.h/6)*(k1 + 2*k2 + 2*k3 + k4)))


		resultado = {
			'x': list(map(lambda val: str(float(val)),x)),
			'yrungekutta': list(map(lambda val: str(float(val)), yf))
		}

		return resultado

	@property
	def rungekutta3(self):
		if self.h == 0 and self.n == 0:
			return "Debes proporcionar al menos un espaciado (h) o un número de puntos (n)"

		if self.h == 0:
			self.h = (float(self.xf) - float(self.x0))/self.n

		if self.n == 0:
			self.n = (float(self.xf) - float(self.x0))/self.h

		x = list(np.linspace(float(self.x0), float(self.xf), int(self.n+1)))

		k1 = float(self.eval(self.x0, self.y0))
		k2 = float(self.eval(self.x0 + (self.h/2),self.y0 + ((self.h * k1)/2)))
		k3 = float(self.eval(self.x0 + self.h,(self.y0 - self.h*k1 + 2*self.h*k2)))

		yf = []
		yf.append(self.y0)
		#primera iteracion de runge kutta
		yf.append(yf[0] + ((self.h/6)*(k1 + 4*k2 + k3)))

		for i in range(2,len(x)):
			k1 = float(self.eval(x[i-1], yf[i-1]))
			k2 = float(self.eval(x[i-1] + (self.h/2),yf[i-1] + ((self.h * k1)/2)))
			k3 = float(self.eval(x[i-1] + self.h,(yf[i-1] - self.h*k1 + 2*self.h*k2)))

			yf.append(yf[i-1] + ((self.h/6)*(k1 + 4*k2 + k3)))

		resultado = {
			'x': list(map(lambda val: str(float(val)),x)),
			'yrungekutta': list(map(lambda val: str(float(val)), yf))
		}
		return resultado

	@property
	def rungekutta2(self):
		if self.h == 0 and self.n == 0:
			return "Debes proporcionar al menos un espaciado (h) o un número de puntos (n)"

		if self.h == 0:
			self.h = (float(self.xf) - float(self.x0))/self.n

		if self.n == 0:
			self.n = (float(self.xf) - float(self.x0))/self.h

		x = list(np.linspace(float(self.x0), float(self.xf), int(self.n+1)))

		k1 = float(self.eval(self.x0, self.y0))
		k2 = float(self.eval(self.x0 + self.h, self.y0 + (self.h*k1)))

		yf = []
		yf.append(self.y0)
		#primera iteracion de runge kutta
		yf.append(yf[0] + ((self.h/2)*(k1 + k2)))

		for i in range(2, len(x)):
			k1 = float(self.eval(x[i-1], yf[i-1]))
			k2 = float(self.eval(x[i-1] + self.h, yf[i-1] + (self.h*k1)))

			yf.append(yf[i-1] + ((self.h/2)*(k1 + k2)))

		resultado = {
			'x': list(map(lambda val: str(float(val)),x)),
			'yrungekutta': list(map(lambda val: str(float(val)), yf))
		}

		return resultado
