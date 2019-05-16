#!/usr/bin/python3

#cuando el identificador empieza con un underscore, significa que es privado: E: class _Internal:
#si tiene 2 underscore significa que es fuertemente privado, sin embargo, no es posible forzar privacidad, solo ponerlo en cosideración
#ya que se puede acceder a identificadores privados con otro método.

def metodo():
	print ("desde metodo")
	return

def otroMetodo():
	a = 5
	b = 7
	return a+b

def manejoListas():
	milista = ['a', 'b', 'c']
	return milista

def recorriendoLista():
	nuevaLista = manejoListas()
	for elemento in nuevaLista:
		print("El elemento es: "+elemento)

def ifEIdentacion():
	var1 = 101
	if (var1 == 100) :
		print ("Es 100")
	else:
		print ("No es 100")

def tiposDeQuotes():
	word = 'word'
	sentence = "This is a sentence."
	paragraph = """This is a paragraph. It is made up of 
	multiple lines and sentences."""
	print (paragraph)




#metodo()
#print (otroMetodo())
#scopelista = manejoListas() #No se puede acceder a la lista directamente porque esta fuera del scope.
#print (scopelista)
#recorriendoLista()
#ifEIdentacion()
tiposDeQuotes()