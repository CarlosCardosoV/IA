#Nombre 1 +iniciales
#Nombre 2 +iniciales
#Nombre 3 +iniciales
#Nombre 4 +iniciales
#CODIFICA Y DECOFICA CORRECTAMENTE CON UNA PALABRA CLAVE SIN PALABRAS REPETIDAS
#CON UNA PALABRA CLAVE CON PALABRAS REPETIDAS CODIFICA CORRECTAMENTE, PERO NO DECODIFICA (ERROR EN LINEA 61 AL INTENTAR ORDENAR POR UN CRITERIO)

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
		[cadena_caracteres,clave_caracteres,clave] = generarListas()
		#Numero de columnas de la tabla	
		columnas = len(clave)				
		renglones = int(math.ceil(float(len(cadena_caracteres)) / float(len(clave))) ) #Cuntas veces cabe la clave en el texto, con un redondeo hacia arriba	
		tabla = generarTabla(renglones,columnas,cadena_caracteres) #Cracion de una tabla
	  		
		#Mostramos la clave y debajo el texto
		print "CLAVE"
		print clave_caracteres
		print "TEXTO"
		for i in tabla:
	  		print i	

	  	m_tabla = matrix(tabla) #Conversion de la tabla a matriz
	  	m_transpuesta = m_tabla.T #Su transpuesta
	  	
		lista_columnas = m_transpuesta.tolist() #De vuelta a una lista
	  	lista_diccionario = generarListaDiccionario(columnas,clave_caracteres,lista_columnas)
	  	lista_diccionario.sort() #Ordenarndo la l en orden alfabetico

	  	#Se intercambian los elementos de la tupla
	  	cadena_codigo = tuple([list(tup) for tup in zip(*lista_diccionario)]) #http://stackoverflow.com/questions/19339/a-transpose-unzip-function-in-python-inverse-of-zip
	  	
	  	print "CADENA CODIFICADA: "
	  	cad = imprimirCadena(cadena_codigo[1])
	  	print cad 

	def decodificar(self):
		[cadena_caracteres,clave_caracteres,clave] = generarListas()

		columnas = len(cadena_caracteres)/len(clave)
		renglones = len(clave)
		
		tabla = generarTabla(renglones,columnas,cadena_caracteres) #Generacion de una tabla 
		m_tabla = matrix(tabla) #Se convierte a una matriz
		m_transpuesta = m_tabla.T #Se obtiene su transpuesta
		clave_caracteres.sort()	#Ordenando la clave en orden alfabetico
		print "CLAVE ORDENADA"
		print clave_caracteres
		print "TABLA"
		print m_transpuesta
		lista_columnas = m_tabla.tolist() #Conversion a lista de la matriz
		lista_diccionario = generarListaDiccionario(renglones,clave_caracteres,lista_columnas) 
		
		#Se ordena el diccionario con el criterio de la palabra clave
		lista_diccionario.sort(key=lambda x: clave.index(x[0])) #http://stackoverflow.com/questions/28668738/sort-list-of-tuples-with-multiple-criteria
		texto = tuple([list(tup) for tup in zip(*lista_diccionario)]) #Se seperan los letras de la palabra clave de la columna asociada 
		matriz_texto = matrix(texto[1])
		m_t_texto = matriz_texto.T

		#Pasamos la matriz a listas
		texto_final = m_t_texto.tolist()
		print "TEXTO DECODIFICADO"
		cad = imprimirCadena(texto_final)
		print cad

	def salir(self):
		print " "

	def limpiar(self):
		os.system('cls')


def generarListas():
	cadena = raw_input("Cadena:")
	clave = raw_input("Palabra clave:")

	#Convierte la clave y el texto en una lista de caracteres
	cadena_caracteres = list(cadena) 					
	clave_caracteres = list(clave)

	#Quita los espacios de la lista de caracteres del texto
	while ' ' in cadena_caracteres:
		cadena_caracteres.remove(' ')	

	return cadena_caracteres,clave_caracteres,clave


def generarTabla(renglones,columnas,cadena_caracteres):
	abecedario = ['A','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	tabla = []
	for i in range(renglones):
		tabla.append([])
		for j in range(columnas):
			tabla[i].append(None)
	aux=0
	for i in range(renglones):
		for j in range(columnas):
			if aux<len(cadena_caracteres):
				tabla[i][j] = cadena_caracteres[aux]
				aux+=1
			else:
			    tabla[i][j] = random.choice(abecedario) #Los espacios vacios(None), los rellena con una letra al azar
	return tabla

def generarListaDiccionario(valor,clave_caracteres,lista_columnas):
	#Asociar cada elemento de la lista_columna con su respectiva letra de la clave (key en el diccionario)
	diccionario = {}
	for i in range(valor):
		if clave_caracteres[i] in diccionario:
		    diccionario[clave_caracteres[i]+str(i)] = lista_columnas[i] #Si ya existe la clave en el diccionario, la renombra con un 'A1' por ejemplo
	  	else:
	  		diccionario[clave_caracteres[i]] = lista_columnas[i]  
	
	#Se reordena la palabra clave junto con sus columnas asociadas 
	lista_diccionario = diccionario.items()
	return lista_diccionario


def imprimirCadena(cadena_codigo):
	cad=''
	for i in cadena_codigo:
		cad = cad+''.join(i)
	return cad

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

