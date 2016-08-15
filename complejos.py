#ESTE PROGRAMA PERMITE REALIZAR LAS SIGUIENTES OPERACIONES CON NUMEROS COMPLEJOS
##MODULO,ANGULO
##SUMA
##RESTA
##MULTIPLICACION
##DIVISION
##POTENCIACION
import sys
import os
import random 
from math import *

print "OPERACIONES CON POLINOMIOS"
class Comandos():	
	def ayuda(self):
		print ">>"
		print("modang: Obtiene el modulo y el angulo de un numero complejo")
		print("sumar: Suma 2 numeros complejos")
		print("restar: Resta 2 numeros complejos")
		print("multiplicar: Multiplica 2 numeros complejos")
		print("dividir: Divide 2 numeros complejos")
		print("potenciar: Potenciacion de un numero complejo")
		print("limpiar: Limpia la consola")
		print("salir: Cerrar la consola")

	def modang(self):
		complejo = obtenerNumero()
		modulo = abs(complejo)
		print "Modulo = %.2f" %modulo
		angulo = degrees(atan2(complejo.imag,complejo.real)) #degrees: conversion de radianes a grados. atan2(y,x) = atan(y/x)
		print "Angulo = %.2f grados"%angulo
	def sumar(self):
		print "Numero complejo1"
		complejo1 = obtenerNumero()
		print "Numero complejo2"
		complejo2 = obtenerNumero()
		suma = complejo1 + complejo2
		imprimirNumero(suma)

	def restar(self):
		print "Numero complejo1"
		complejo1 = obtenerNumero()
		print "Numero complejo2"
		complejo2 = obtenerNumero()
		resta = complejo1 - complejo2
		imprimirNumero(resta)

	def multiplicar(self):
		print "Numero complejo1"
		complejo1 = obtenerNumero()
		print "Numero complejo2"
		complejo2 = obtenerNumero()
		producto = complejo1 * complejo2
		imprimirNumero(producto)
		
	def dividir(self):
		print "Numero complejo1"
		complejo1 = obtenerNumero()
		print "Numero complejo2"
		complejo2 = obtenerNumero()
		division = complejo1 / complejo2
		imprimirNumero(division)
	
	def potenciar(self):
		complejo = obtenerNumero()
		exponente = input("Ingresa exponente: ")
		potencia = complejo**exponente
		imprimirNumero(potencia)
	
	def salir(self):
		print " "

	def limpiar(self):
		os.system('cls')

def imprimirNumero(resultado):	
	print "Resultado = "
	print resultado
def obtenerNumero():
	complejo = input("Ingresa un numero complejo (ejemplo: %+d %+dj): " %(random.randrange(-10,10),random.randrange(-10,10))) 
	return complejo

#Imitacion de una consola de comandos
#Los comandos con sus respectivos metodos se almacenan en un directorio para utilizarlo como un switch
def shell():
	print"\n"
	print ">>"
	print "Teclear ayuda para ver lista de comandos"
	cmd = Comandos()
	comando = "entrar" #PARA ENTRAR AL CICLO
	while(comando != "salir"):
		comandos = {'ayuda': cmd.ayuda,'modang':cmd.modang,'sumar':cmd.sumar,'restar':cmd.restar,'multiplicar':cmd.multiplicar,'dividir':cmd.dividir,'potenciar':cmd.potenciar,'limpiar': cmd.limpiar, 'salir': cmd.salir }
		comando = raw_input('>>')
		
		try:
			comandos[comando]()
		except:
			print (" %s no se reconoce como un comando. Teclea 'ayuda' para ver lista de comandos" %comando)

shell()