#!/usr/bin/python3

contador = 100          # integer
kilometros   = 1000.0   # float
nombre    = "Esteban"   # string

print (contador)
print (kilometros)
print (nombre)

#asignacion multiple

a = b = c = 1
d,e,f = 1,2.0,"Esteban"

print (a,b,c,d,e,f)

#borrando referencias
del a, e

#print (a,b,c,d,e,f) #esto bota la ejecucion en "a", por eso se comenta

x = ["manzana", "platano", "cherry"]
del x[0]
print(x) #manzana no está

#Tipos de datos estandar en Python: Numbers, String, List, Tuple, Dictionary
#Tipos de numeros: int, long, float, complex