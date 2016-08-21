#tabla = np.matrix(clave,texto)
#Creacion de n listas segun el numero de letras de la clave
#a = list(palabra)

#[c for c in "foobar"]
#list parte una cadena de texto por un separador.
from numpy import matrix
import math 
import random




class Comandos():	
	def ayuda(self):
		print ">>"
		print("codificar: Obtiene una cadena cifrada de un texto dada una clave")
		print("decodificar: Obtiene un mensaje dada una cadena cifrada y una clave")
		print("limpiar: Limpia la consola")
		print("salir: Cerrar la consola")


	def codificar(self):
		texto = raw_input("Texto a codificar:")
		clave = raw_input("Palabra clave:")
		
		abecedario = ['A','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
		#Convierte la clave y el texto en una lista de caracteres
		texto_caracteres = list(texto) 					
		clave_caracteres = list(clave)

		#Quita los espacios de la lista de caracteres del texto
		while ' ' in texto_caracteres:
			texto_caracteres.remove(' ')	

		#Numero de columnas de la tabla	
		columnas = len(clave)				
		renglones = int(math.ceil(float(len(texto_caracteres)) / float(len(clave))) ) #Cuntas veces cabe la clave en el texto, con un redondeo hacia arriba	

		#Cracion de la tabla
		tabla = []
		for i in range(renglones):
			tabla.append([])
			for j in range(columnas):
				tabla[i].append(None)
	  	
	  	#Llenado de la tabla con el texto que ingreso el usuario
	  	aux=0
	  	for i in range(renglones):
	  		for j in range(columnas):
	  			if aux<len(texto_caracteres):
	  				tabla[i][j] = texto_caracteres[aux]  
					aux+=1
				else:
					tabla[i][j] = random.choice(abecedario) #Los espacios vacios(None), los rellena con una letra al azar
		
		#Mostramos la clave y debajo el texto
		print "CLAVE"
		print clave_caracteres
		print "TEXTO"
		for i in tabla:
	  		print i	

	  	#Conversion de la tabla a matriz
	  	m_tabla = matrix(tabla)
	  	m_transpuesta = m_tabla.T
	  	
		lista_columnas = m_transpuesta.tolist() #De vuelta a una lista
	   	
	  	#Asoaciar cada elemento de la lista_columna con su respectiva letra de la clave
	  	diccionario = {}
	  	for i in range(columnas):
	  		diccionario[clave_caracteres[i]] = lista_columnas[i]  #===>FALLA: si se repite una letra de la clave el diccionario sobreescribira su key.  
	  	
	  	#print "Diccionario desordenado"
	  	#print diccionario

	  	#Ordenar el diccionario en orden alfabetico
	  	lista_diccionario = diccionario.items()
	  	lista_diccionario.sort()
	  	
	  	#print "Diccionario ordenado"
	  	#print lista_diccionario

	  	#Se intercambian los elementos de la tupla
	  	cadena_codigo = tuple([list(tup) for tup in zip(*lista_diccionario)]) #http://stackoverflow.com/questions/19339/a-transpose-unzip-function-in-python-inverse-of-zip
	  	
	  	print "CODIGO: "
	  	print cadena_codigo[1]

	def decodificar():
		texto = raw_input("Texto a codificar: ")
		clave = raw_input("Palabra clave: ")

	def salir(self):
		print " "

	def limpiar(self):
		os.system('cls')


def shell():
	print"\n"
	print ">>"
	print "Teclear ayuda para ver lista de comandos"
	cmd = Comandos()
	comando = "entrar" #PARA ENTRAR AL CICLO
	while(comando != "salir"):
		comandos = {'ayuda': cmd.ayuda,'codificar':cmd.codificar,'decodificar':cmd.decodificar,'limpiar': cmd.limpiar, 'salir': cmd.salir }
		comando = raw_input('>>')
		
		try:
			comandos[comando]()
		except:
			print (" '%s' no se reconoce como un comando. Teclea 'ayuda' para ver lista de comandos" %comando)

shell()

#Posible soluacion a la repeticion de keys en los diccionarios
#from collections import defaultdict
#d = defaultdict(list)
#d[a].append(b)

#Si ya exite la clave renombrala como AB, EB, etc