#BSME: Beltran Sarmiento Mario Edwin 
#CVCE: Cardoso Valencia Carlos ErIc 
#MPVS: Martinez Pozos Victor Sebastian 
#MI: Marin Ivan


import random

def granSuperVillano(numero_villanos,numero_superVillanos):
	
	habilidades = ["MALDAD","VOLAR","FUERZA","EGO","MONOLOGAR","TRIUNFOS","INGENIO","PODER MENTAL","AUDACIA","PODER ECONOMICO"]
	columnas = len(habilidades)
	renglones = numero_villanos
	tabla = primeraGeneracion(renglones,columnas)   #PASO 1: GENERAR UNA PRIMERA GENERACION
	
	#Mostramos la tabla de la primera generacion de villanos	
	print habilidades
	for i in tabla:
		print i

	megamente = [None]*columnas #Almacena las habilidades de todos los Megamentes
	sedusa = [None]*columnas #Almacena las habilidades de todos las Sedusas
	sedumente = [None]*columnas #Almacena las habilidades de todos los Sedumentes
	aleatorio = [None]*columnas

	#Repetir pasos 2,3,4 para tener 10 Sedumentes (PASO 5)
	for i in range(numero_superVillanos):
		megamente[i] = crearNuevoVillano(tabla,renglones,columnas) #PASO 2: CREACION DE UN NUEVO VILLANO1 DADA LA PRIMERA GENERACION
		print "Habilidades Megamente %d" %(i+1)
		print megamente[i]

		sedusa[i] = crearNuevoVillano(tabla,renglones,columnas) #PASO 3: CREACION DE UN NUEVO VILLANO2 DADA LA PRIMERA GENERACION
		print "Habilidades Sedusa %d" %(i+1)
		print sedusa[i]

		[ sedumente[i],aleatorio[i] ]= mezclarVillanos(megamente[i],sedusa[i],columnas) #PASO 4. Mezclar las habilidades de los anteriores 2 super villanos 
																								#dado un numero aleatorio genera un nuevo supervillano 
																								#Megamente[i] +Sedusa[i] = Sedumente[i]
		print "Habilidades Sedumente[%d]. (Mezcla de Megamente %d y Sedusa %d con aleatorio %d)" %((i+1),(i+1),(i+1),aleatorio[i])
		print sedumente[i]

	#PASO 6 (aplicar los pasos 2,3,4) sobre la poblacion de 10 supervillanos (sedumentes)
	super_Villano1 = crearNuevoVillano(sedumente,numero_superVillanos,columnas)  #Creacion de Gran supervillano1 dada la tabla de Supervillanos (Sedumentes) 
	super_Villano2 = crearNuevoVillano(sedumente,numero_superVillanos,columnas)  #Creacion de Gran supervillano2 dada la tabla de Supervillanos

	[granVillano,aleatorio] = mezclarVillanos(super_Villano1,super_Villano2,columnas) #Mezcla de las habilidades de los anteriores dos supervillanos generea
	
	print "Gran Supervillano1 dada la generacion de Sedumentes"
	print super_Villano1
	print "Gran Supervillano2 dada la generacion de Sedumentes"
	print super_Villano2
	print "El mejor Supervillano (Gran Supervillano1 + Gran Supervillano2)con Aleatorio = %d es:" %(aleatorio)					#El GRAN VILLANO (hijo de superVillano1+supervillano2)
	print granVillano


#Crea una primera generacion de villanos con habilidades aleatorias del 0 al 9. 
def primeraGeneracion(renglones,columnas):
	tabla = []
	for i in range(renglones):
		tabla.append([])
		for j in range(columnas):
			tabla[i].append(None)

	for i in range(renglones):
		for j in range(columnas):
			tabla[i][j] =random.randrange(10) #Numeros aleatorios del 0 al 9	 
	return tabla

#Crea un nuevo villano a partir de los datos de una tabla
def crearNuevoVillano(tabla,renglones,columnas):
	habilidades_villano = [None]*columnas #Creacion de una lista que almacene los valores de cada habilidad del nuevo villano. 
	for i in range(columnas):
		habilidades_villano[i] = tabla[random.randrange(renglones)][i] #Para llenar cada habilidad del nuevo villano tomando aleatoriamente los valores sobre cada habilidad
	return habilidades_villano

#Genera un supervillano, la mezcla entre dos villanos que se generaron de la primera generacion
def mezclarVillanos(habilidades_villano1,habilidades_villano2,columnas):
	aleatorio = random.randint(1,10)
	habilidades_superVillano = [None]*columnas
	for i in range(columnas):
		if i+1<=aleatorio:
			habilidades_superVillano[i] = habilidades_villano1[i]      #Aqui nos aseguramos que dado las habiliades del nuevo supervillano se repartan entre 
		else:															#las del primer y segundo villanos dado un numero aleatorio
			habilidades_superVillano[i] = habilidades_villano2[i]

	return habilidades_superVillano,aleatorio



numero_villanos = input("Numero de villanos iniciales: ")
numero_superVillanos = input("Numero de supervillano(Sedumentes)")
granSuperVillano(numero_villanos,numero_superVillanos)