import math
from sympy import *
class Sinhx:
    def __init__(self, cifras, x):
            self.cifras = cifras
            self.x = sympify(x)
            self.aproximaciones = []
            self.errores = []
    @property
    def sinhx(self):
        #Error de tolerancia
        Ess = 0.5 * (10**(2 - self.cifras));
        ea = 1000
        aproximacionActual = 0
        n=0
        while ea > Ess: 
            self.aproximaciones.append(aproximacionActual)
            aproximacionAnterior = aproximacionActual
            aproximacionActual = aproximacionActual + (math.pow(self.x,(2*n+1))/math.factorial(2*n+1))
            ea = abs((aproximacionActual-aproximacionAnterior)/aproximacionActual)*100
            self.errores.append(ea)
            n = n + 1
        resultado = {
            'Aproximaciones': self.aproximaciones,
            'Errores': self.errores,
        }
        return resultado