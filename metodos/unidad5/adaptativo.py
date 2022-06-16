from sympy import *
from .rungekutta import RungeKutta

class Adaptativo(RungeKutta):
	def __init__(self,f, x0,y0,xf,h = 0,n = 0, pasos = 4):
		RungeKutta.__init__(self,f,x0,y0,xf,h,n)
		self.pasos = pasos

	@property
	def adaptativo(self):
		x = []
		ykutta = []

		if self.pasos == 2:
			rkutta = self.rungekutta2
			if rkutta == "666":
				return "666"
			x = rkutta['x']
			ykutta = rkutta['yrungekutta']
		elif self.pasos == 3:
			rkutta = self.rungekutta3
			if rkutta == "666":
				return "666"
			x = rkutta['x']
			ykutta = rkutta['yrungekutta']
		else:
			rkutta = self.rungekutta4
			if rkutta == "666":
				return "666"
			x = rkutta['x']
			ykutta = rkutta['yrungekutta']

		x = list(map(lambda val: float(val),x))
		ykutta = list(map(lambda val: float(val), ykutta))
		
		values = []
		for i in range(len(x) - 1):
			values.append(self.eval(x[i],ykutta[i]))

		if self.pasos == 4:
			predictor = ykutta[self.pasos - 1] + ((self.h/24)*(55*values[-1] - 59*values[-2] + 37*values[-3] - 9*values[-4]))
		elif self.pasos == 3:
			predictor = ykutta[self.pasos - 1] + ((self.h/12)*(23*values[-1] - 16*values[-2] + 5*values[-3]))
		else:
			predictor = ykutta[self.pasos - 1] + ((self.h/2)*(3*values[-1] - values[-2]))

		values.append(self.eval(self.xf,predictor))

		if self.pasos == 4:
			corrector = ykutta[self.pasos - 1] + ((self.h/24)*(9*values[-1] + 19*values[-2] - 5*values[-3] + values[-4]))
		elif self.pasos == 3:
			corrector = ykutta[self.pasos - 1] + ((self.h/12)*(5*values[-1] + 8*values[-2] - values[-3]))
		else:
			corrector = ykutta[self.pasos - 1] + ((self.h/2)*(values[-1] + values[-2]))

		values.pop() # se elimina el elemento del predictor
		values.append(corrector) # y se agrega el elemento del corrector

		resultado = {
			'x': list(map(lambda val: str(float(val)),x)),
			'yadaptativo': list(map(lambda val: str(float(val)), values))
		}

		return resultado
