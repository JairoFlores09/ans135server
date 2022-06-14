from sympy import *
import numpy as np

class Lagrange:
    def __init__(self,xi,evalu,funct='',fi=[]):
        self.funct = funct
        self.xi = list(map(lambda x: float(x), xi))
        self.fi = list(map(lambda x: float(x), fi))
        self.polinomio = []
        self.evaluacion = []
        self.evalu = float(evalu)
    
    def eval(self, valor):
        x = symbols('x')
        return self.funct.subs(x,float(valor))

    @property
    def lagrange(self):
        x = symbols('x')
        n = len(self.xi)
        if len(self.funct) != 0:
            self.funct = sympify(self.funct.replace("^","**"))
            self.fi = []
            for i in range(0,n):
                self.fi.append(float(self.eval(self.xi[i])))
        polinomio = 0
        divisorL = np.zeros(n, dtype = float)
        for i in range(0,n,1):
            numerador = 1
            denominador = 1
            for j  in range(0,n,1):
                if (j!=i):
                    numerador = numerador*(x-self.xi[j])
                    denominador = denominador*(self.xi[i]-self.xi[j])
            terminoLi = numerador/denominador
            polinomio = polinomio + terminoLi*self.fi[i]
            divisorL[i] = denominador
        polisimple = polinomio.expand()
        sustitucion = polisimple.subs(x,self.evalu) 
        polisimple = str(polisimple) 
        polisimple = polisimple.replace("**","^")
        polisimple = polisimple.replace("*","")
        resultado = {
                        "Polinomio": [str(polisimple)],
                        "Interpolación": [str(sustitucion)]
                    }
        return resultado

