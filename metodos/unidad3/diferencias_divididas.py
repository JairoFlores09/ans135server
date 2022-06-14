from sympy import *
import numpy as np

class DiferenciasDivididas: 

    def __init__(self, xi,evalu, funct='', fi=[]):
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
    def diferencias_divididas(self):
        x = symbols('x')
        n = len(self.xi)
        if len(self.funct) != 0:
            self.funct = sympify(self.funct.replace("^","**"))
            self.fi = []
            for i in range(0,n):
                self.fi.append(float(self.eval(self.xi[i])))
        ki = np.arange(0,n,1)
        tabla = np.concatenate(([ki],[self.xi],[self.fi]),axis=0)
        tabla = np.transpose(tabla)
        dfinita = np.zeros(shape=(n,n),dtype=float)
        tabla = np.concatenate((tabla,dfinita), axis=1)
        [n,m] = np.shape(tabla)
        diagonal = n-1
        j = 3
        while (j < m):
            i = 0
            paso = j-2 
            while (i < diagonal):
                denominador = (self.xi[i+paso]-self.xi[i])
                numerador = tabla[i+1,j-1]-tabla[i,j-1]
                tabla[i,j] = numerador/denominador
                i = i+1
            diagonal = diagonal - 1
            j = j+1
        dDividida = tabla[0,3:]
        n = len(dfinita)
        polinomio = self.fi[0]
        for j in range(1,n,1):
            factor = dDividida[j-1]
            termino = 1
            for k in range(0,j,1):
                termino = termino*(x-self.xi[k])
            polinomio = polinomio + termino*factor
        polisimple = polinomio.expand()
        sustitucion = polisimple.subs(x,self.evalu)
        polisimple = str(polisimple)
        polisimple = polisimple.replace("**","^")
        polisimple = polisimple.replace("*","")
        resultado = {
                        "Polinomio": [polisimple],
                        "Interpolación": [str(sustitucion)]
                    }
        return resultado