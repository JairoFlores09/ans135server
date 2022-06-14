import math 

class Fraccion: 
 	def __init__(self,x,cifras): 
 		self.cifras = cifras
 		self.x = x 
 		self.aproximaciones = [] 
 		self.error = [] 

 	@property
 	def fraccion(self):
 			# Error de tolerancia 
 			Ess = 0.5*(10**(2-self.cifras)); 
 			Ea = 1000 
 			aproximacionActual = 1  
 			n = 1

 			while(Ea > Ess):

 				aproximacionAnterior = aproximacionActual

 				#aproximacionActual +=  ((-1)**n)*(self.x**(2*n))

 				aproximacionActual += self.x**(n)

 				self.aproximaciones.append(aproximacionActual)

 				Ea = abs((aproximacionActual - aproximacionAnterior)/aproximacionActual) * 100

 				self.error.append(Ea)

 				n += 1

 			resultado = {
 				'Aproximaciones': self.aproximaciones,
 				'Errores': self.error
 			}

 			return resultado