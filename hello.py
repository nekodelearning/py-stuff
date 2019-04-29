#!/usr/bin/python3

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


    
var1 = 101
if (var1 == 100) :
    print ("Es 100")
else:
    print ("No es 100")



metodo()
print (otroMetodo())
scopelista = manejoListas() #No se puede acceder a la lista directamente porque esta fuera del scope.
print (scopelista)
recorriendoLista()
	