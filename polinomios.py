######################################################################################################################################
##	OPERACIONES CON POLINIOMIOS																										##
##	ALUMNO: CARDOSO VALENCIA CARLOS ERIC 	                                                                                        ##                    		##
##  INTELIGENCIA ARTIFICIAL GRUPO                                                                 		                     		##
##  																																##
##  ESTE PROGRAMA PERMITE REALIZAR LAS SIGUIENTES OPERACIONES CON POLINOMIOS DE GRADO N DE UNA VARIABLE								##
##		VALOR EN UN PUNTO 																											##
##		SUMA 																														##
##		RESTA 																														##		
##		MULTIPLICACION 																												##
##		DERIVACION 																													##
## 		INTEGRACION
## A TRAVES DE UNA SIMULACION DE CONSOLA, MODULO NUMPY,BLA BLA BLA
## http://docs.scipy.org/doc/numpy/reference/routines.polynomials.polynomial.html
##FALTA INTEGRAR LOS METODOS EN UNA CLASE LLAMADA POLINOMIO?


from numpy.polynomial import polynomial as pol
import sys
import os

print "OPERACIONES CON POLINOMIOS"
class Comandos():	
	def ayuda(self):
		print ">>"
		print("valuar: Valuar un polinomio en un punto dado")
		print("sumar: Suma dos polinomios")
		print("restar: Resta dos polinomios")
		print("multiplicar: Multiplica dos polinomios")
		print("derivar: Obtiene la derivada de un polinomio.")
		print("integrar: Calcula la integral de un polinomio")
		print("limpiar: Limpia la consola")
		print("salir: Cerrar la consola")

	def valuar(self):
		coeficientes = obtenerPolinomio()			
		valor = input("Valuar en x=")
		print "P(x) = "
		imprimirPolinomio(coeficientes) 		
   		polinomio_valuado = pol.polyval(valor,coeficientes)
		print ("\nP(%.2f) = %d" %(valor,polinomio_valuado))
		
	def sumar(self):
		print "Polinomio 1"
		coeficientes1 = obtenerPolinomio()
		print"Polinomio 2"
		coeficientes2 = obtenerPolinomio()	
		polinomio_suma = pol.polyadd(coeficientes1, coeficientes2)
		print "P_suma(x) = "
		imprimirPolinomio(polinomio_suma)

	def restar(self):
		print "Polinomio 1"
		coeficientes1 = obtenerPolinomio()
		print"Polinomio 2"
		coeficientes2 = obtenerPolinomio()
		polinomio_resta = pol.polysub(coeficientes1, coeficientes2)
		print "P_resta(x) = "
		imprimirPolinomio(polinomio_resta)
	
	def multiplicar(self):
		print "Polinomio 1"
		coeficientes1 = obtenerPolinomio()
		print"Polinomio 2"
		coeficientes2 = obtenerPolinomio()
		polinomio_multiplicacion = pol.polymul(coeficientes1, coeficientes2)
		print "P_producto(x) = "
		imprimirPolinomio(polinomio_multiplicacion)
	
	def derivar(self):
		coeficientes = obtenerPolinomio()
		polinomio_derivado = pol.polyder(coeficientes)
		print "P_derivado(x) = "
		imprimirPolinomio(polinomio_derivado)
	
	def integrar(self):
		coeficientes = obtenerPolinomio()		
		polinomio_integrado = pol.polyint(coeficientes)
		print "P_integrado(x) = "
		imprimirPolinomio(polinomio_integrado)

	def salir(self):
		print " "

	def limpiar(self):
		os.system('cls')

def imprimirPolinomio(coeficientes):
	for i in range(len(coeficientes)):
		sys.stdout.write("%+.2fx^%d "%(coeficientes[i],i)) #Impresion en una sola linea
   		sys.stdout.flush()		
   	print " "

def obtenerPolinomio():
	grado = input("Grado del polinomio: ")
	coeficientes = [0]*(grado+1)
	for i in range(0,grado+1):	
		coeficientes[i] = input("Coeficiente %d: " %i)
	return coeficientes

#Imitacion de una consola de comandos
#Los comandos con sus respectivos metodos se almacenan en un directorio para utilizarlo como un switch
def shell():
	print"\n"
	print ">>"
	print "Teclear ayuda para ver lista de comandos"
	cmd = Comandos()
	comando = "entrar" #PARA ENTRAR AL CICLO
	while(comando != "salir"):
		comandos = {'ayuda': cmd.ayuda,'valuar':cmd.valuar,'sumar':cmd.sumar,'restar':cmd.restar,'multiplicar':cmd.multiplicar,'derivar':cmd.derivar,'integrar':cmd.integrar,'limpiar': cmd.limpiar, 'salir': cmd.salir }
		comando = raw_input('>>')
		
		try:
			comandos[comando]()
		except:
			print (" %s no se reconoce como un comando. Teclea 'ayuda' para ver lista de comandos" %comando)

shell()